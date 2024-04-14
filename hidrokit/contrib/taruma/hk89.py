"""
hk89: hydrological_model_nreca

This module contains the implementation of the NRECA hydrological model calculations.

The NRECA hydrological model is used to calculate various hydrological parameters such as storage, 
    groundwater recharge, evapotranspiration, water balance, flow, and discharge. 
    The model takes precipitation and evapotranspiration data as input and 
    performs calculations based on various coefficients and parameters.

The main function in this module is `model_NRECA`, 
    which performs the NRECA hydrological model calculations on the given data.

For more information about the model and its calculations, refer to the manual available at:
https://gist.github.com/taruma/1502a7aa67cf074969d806cd3ffdf35c
"""

import warnings
import numpy as np
import pandas as pd


# pylint: disable=invalid-name
def _STORAT(STORAGE, NOMINAL):
    return STORAGE / NOMINAL


def _STORAGE(STORAGE, DELSTOR):
    return STORAGE + DELSTOR


def _PRERAT(PRECIP, PET):
    return PRECIP / PET


def _ETRAT(STORAT, PRERAT):
    VAL = (STORAT / 2) + ((1 - (STORAT / 2)) * PRERAT)
    return VAL if VAL < 1 else 1


def _AET(ETRAT, PET, CF=1):
    return ETRAT * PET * CF


def _WATBAL(PRECIP, AET):
    return PRECIP - AET


def _EXMRAT(WATBAL, STORAT):
    if WATBAL < 0:
        return 0
    if STORAT > 1:
        return 1 - (0.5 * (2 - STORAT) ** 2)
    else:
        return 0.5 * (STORAT**2)


def _EXMST(EXMRAT, WATBAL):
    return EXMRAT * WATBAL


def _DELSTOR(WATBAL, EXMST):
    return WATBAL - EXMST


def _GWRECH(PSUB, EXMST):
    return PSUB * EXMST


def _GWSTOR2(GWSTOR_1, GWRECH):
    return GWSTOR_1 + GWRECH


def _GWSTOR1(GWSTOR_2, GWFLOW):
    return GWSTOR_2 - GWFLOW


def _GWFLOW(GWRAT, GWSTOR_2):
    return GWRAT * GWSTOR_2


def _DFLOW(EXMST, GWRECH):
    return EXMST - GWRECH


def _FLOW(GWFLOW, DFLOW):
    return GWFLOW + DFLOW


def _DISCHARGE(FLOW, AREA, DAYS):
    return (FLOW / 1000) * AREA / (DAYS * 24 * 60 * 60)


def _NOMINAL(C, PRECIP_MEAN_ANNUAL):
    return 100 + C * PRECIP_MEAN_ANNUAL


# pylint: disable=too-many-arguments,too-many-locals,too-many-statements,too-many-branches
def model_NRECA(
    dataframe,
    precipitation_column,
    pevapontraspiration_column,
    MSTOR,
    GSTOR,
    PSUB,
    GWF,
    CF,
    C,
    AREA,
    return_as_dataframe=True,
    report="discharge",
    as_df=None,
    precip_col=None,
    pet_col=None,
):
    """
    Perform the NRECA hydrological model calculations on the given data.

    Args:
        dataframe (pandas.DataFrame): The input data containing precipitation and
            evapotranspiration values.
        precipitation_column (str): The name of the column in the dataframe
            containing precipitation values.
        pevapontraspiration_column (str): The name of the column in the dataframe
            containing evapotranspiration values.
        MSTOR (float): The initial storage value.
        GSTOR (float): The initial groundwater storage value.
        PSUB (float): The groundwater recharge coefficient.
        GWF (float): The groundwater flow coefficient.
        CF (float): The crop factor.
        C (float): The runoff coefficient.
        AREA (float): The area of the catchment.
        return_as_dataframe (bool, optional): Whether to return the results as a
            pandas DataFrame. Defaults to True.
        report (str, optional): The type of report to generate. Possible values are
            'full', 'partial', 'flow', and 'discharge'. Defaults to 'discharge'.
        as_df (bool, optional): Deprecated argument. Use `return_as_dataframe`
            instead. Defaults to None.

    Returns:
        Union[pandas.DataFrame, numpy.ndarray]: The calculated results. If
        `return_as_dataframe` is True, a pandas DataFrame is returned. Otherwise,
        a numpy ndarray is returned.

    Raises:
        ValueError: If an invalid value is provided for the `report` argument.

    """

    if as_df is not None:
        warnings.warn("`as_df` is deprecated. Use `return_as_dataframe` instead.")
        return_as_dataframe = as_df
    if pet_col is not None:
        warnings.warn(
            "`pet_col` is deprecated. Use `pevapontraspiration_column` instead."
        )
        pevapontraspiration_column = pet_col
    if precip_col is not None:
        warnings.warn("`precip_col` is deprecated. Use `precipitation_column` instead.")
        precipitation_column = precip_col

    # sub_df
    data = dataframe.loc[:, [precipitation_column, pevapontraspiration_column]]

    # info df
    nrows = data.shape[0]

    # initialization
    storage, storat, prerat = (np.zeros(nrows) for _ in range(3))
    etrat, aet, watbal = (np.zeros(nrows) for _ in range(3))
    exmst, exmrat, delstor, gwrech = (np.zeros(nrows) for _ in range(4))
    gwstor1, gwstor2, gwflow = (np.zeros(nrows) for _ in range(3))
    dflow, flow, discharge = (np.zeros(nrows) for _ in range(3))

    # calculation
    precip_mean_annual = (
        data[precipitation_column].groupby(by=data.index.year).sum().mean()
    )
    nominal = _NOMINAL(C, precip_mean_annual)

    days = data.index.days_in_month
    precip = data.iloc[:, 0].values
    pet = data.iloc[:, 1].values

    for i in range(nrows):

        if i != 0:
            storage[i] = _STORAGE(storage[i - 1], delstor[i - 1])
        else:
            storage[i] = _STORAGE(MSTOR, 0)

        storat[i] = _STORAT(storage[i], nominal)
        prerat[i] = _PRERAT(precip[i], pet[i])
        etrat[i] = _ETRAT(storat[i], prerat[i])
        aet[i] = _AET(etrat[i], pet[i], CF=CF)
        watbal[i] = _WATBAL(precip[i], aet[i])
        exmrat[i] = _EXMRAT(watbal[i], storat[i])
        exmst[i] = _EXMST(exmrat[i], watbal[i])
        delstor[i] = _DELSTOR(watbal[i], exmst[i])
        gwrech[i] = _GWRECH(PSUB, exmst[i])

        if i != 0:
            gwstor1[i] = _GWSTOR1(gwstor2[i - 1], gwflow[i - 1])
        else:
            gwstor1[i] = _GWSTOR1(GSTOR, 0)

        gwstor2[i] = _GWSTOR2(gwstor1[i], gwrech[i])
        gwflow[i] = _GWFLOW(GWF, gwstor2[i])
        dflow[i] = _DFLOW(exmst[i], gwrech[i])
        flow[i] = _FLOW(gwflow[i], dflow[i])
        discharge[i] = _DISCHARGE(flow[i], AREA, days[i])

    # results
    if report.lower() == "full":
        results = np.stack(
            (
                days,
                precip,
                pet,
                storage,
                storat,
                prerat,
                etrat,
                aet,
                watbal,
                exmrat,
                delstor,
                gwrech,
                gwstor1,
                gwstor2,
                gwflow,
                dflow,
                flow,
                discharge,
            ),
            axis=1,
        )
        columns_name = [
            "DAYS",
            "PRECIP",
            "PET",
            "STORAGE",
            "STORAT",
            "PRERAT",
            "ETRAT",
            "AET",
            "WATBAL",
            "EXMRAT",
            "DELSTOR",
            "GWRECH",
            "GWSTOR1",
            "GWSTOR2",
            "GWFLOW",
            "DFLOW",
            "FLOW",
            "DISCHARGE",
        ]
    elif report.lower() == "partial":
        results = np.stack((precip, pet, storage, gwstor2, flow, discharge), axis=1)
        columns_name = ["PRECIP", "PET", "STORAGE", "GWSTOR2", "FLOW", "DISCHARGE"]
    elif report.lower() == "flow":
        results = flow
        columns_name = ["FLOW"]
    elif report.lower() == "discharge":
        results = discharge
        columns_name = ["DISCHARGE"]
    else:
        raise ValueError(
            str(report) + " not identified. " + "Use full / partial / flow / discharge."
        )

    if return_as_dataframe:
        return pd.DataFrame(data=results, index=data.index, columns=columns_name)
    return results

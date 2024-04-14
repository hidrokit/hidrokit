"""
hk96: hydrological_model_FJMock 
FJMock Model Hydrological Model.

This module implements the FJMock model, 
    which is a hydrological model used for performing calculations related to water flow and 
    other hydrological parameters.

The main function in this module is `model_FJMOCK`, 
    which takes a DataFrame containing the necessary data and 
    performs the calculations based on the FJMock model. 
    The function returns the calculated results based on the specified report type.

For more information about the FJMock model, refer to the following manual:
- https://gist.github.com/taruma/ae5c0209ef19b088e3cd9dd22508af5c
"""

import numpy as np
import pandas as pd


# pylint: disable=invalid-name
def _EPM(NDAYS, EP):
    return NDAYS * EP


def _RATEPM(EXSURF, NRAIN):
    return (EXSURF / 100 / 20) * (18 - NRAIN)


def _DELTAE(RATEPM, EPM):
    return RATEPM * EPM


def _EA(EPM, DELTAE):
    return EPM - DELTAE


def _PEA(PRECIP, EA):
    return PRECIP - EA


def _SMS(PEA, SMC_prev):
    return PEA + SMC_prev


def _SMC(PEA, SMS):
    return 200 if PEA >= 0 else SMS


def _SS(PEA):
    return 0 if PEA >= 0 else PEA


def _WATSUR(PEA, SS):
    return PEA - SS


def _I(WATSUR, IF):
    return WATSUR * IF


def _CAL0(K, I):
    return 1 / 2 * (1 + K) * I


def _CALGS(K, GS_prev):
    return K * GS_prev


def _GS(CAL0, CALGS):
    return CAL0 + CALGS


def _DGS(GS, GS_prev):
    return GS - GS_prev


def _BFLOW(I, DGS):
    return I - DGS


def _DRO(WATSUR, I):
    return WATSUR - I


def _SRO(PRECIP, PF):
    return 0 if PRECIP >= 200 else PRECIP * PF


def _TRO(BFLOW, DRO, SRO):
    return BFLOW + DRO + SRO


def _FLOW(TRO, AREA, NDAYS):
    return (TRO / 1000) * AREA / (NDAYS * 24 * 3600)


# pylint: disable=too-many-arguments, too-many-locals, too-many-branches, too-many-statements
def model_FJMOCK(
    df,
    precip_col,
    ep_col,
    nrain_col,
    ndays_col,
    EXSURF,
    IF,
    K,
    PF,
    ISMC,
    GSOM,
    AREA,
    as_df=True,
    report="flow",
):
    """
    Perform calculations based on the FJMOCK model.

    Args:
        df (pandas.DataFrame): The input DataFrame containing the data.
        precip_col (str): The column name for precipitation data.
        ep_col (str): The column name for evapotranspiration data.
        nrain_col (str): The column name for total-rainfall data.
        ndays_col (str): The column name for number of days data.
        EXSURF (float): The EXSURF value.
        IF (float): The IF value.
        K (float): The K value.
        PF (float): The PF value.
        ISMC (float): The ISMC value.
        GSOM (float): The GSOM value.
        AREA (float): The AREA value.
        as_df (bool, optional): Whether to return the results as a DataFrame.
            Defaults to True.
        report (str, optional):
            The type of report to generate.
            Can be 'full', 'partial', 'tro', or 'flow'. Defaults to 'flow'.

    Returns:
        pandas.DataFrame or numpy.ndarray:
            The calculated results based on the specified report type.
    """

    # sub_df
    data = df.loc[:, [precip_col, nrain_col, ndays_col, ep_col]]
    data_array = data.values

    # info_df
    nrows = data.shape[0]

    # initialization
    (
        epm,
        ratepm,
        deltae,
        ea,
        pea,
        sms,
        smc,
        ss,
        watsur,
        i,
        cal0,
        calgs,
        gs,
        dgs,
        bflow,
        dro,
        sro,
        tro,
        flow,
    ) = (np.zeros(nrows) for _ in range(19))

    # calculation
    precip = data_array[:, 0]
    nrain = data_array[:, 1]
    ndays = data_array[:, 2]
    ep = data_array[:, 3]

    for j in range(nrows):

        epm[j] = _EPM(ndays[j], ep[j])
        ratepm[j] = _RATEPM(EXSURF, nrain[j])
        deltae[j] = _DELTAE(ratepm[j], epm[j])
        ea[j] = _EA(epm[j], deltae[j])
        pea[j] = _PEA(precip[j], ea[j])

        if j == 0:
            sms[j] = _SMS(pea[j], ISMC)
        else:
            sms[j] = _SMS(pea[j], smc[j - 1])

        smc[j] = _SMC(pea[j], sms[j])
        ss[j] = _SS(pea[j])
        watsur[j] = _WATSUR(pea[j], ss[j])
        i[j] = _I(watsur[j], IF)

        cal0[j] = _CAL0(K, i[j])

        if j == 0:
            calgs[j] = _CALGS(K, GSOM)
        else:
            calgs[j] = _CALGS(K, gs[j - 1])

        gs[j] = _GS(cal0[j], calgs[j])

        if j == 0:
            dgs[j] = _DGS(gs[j], GSOM)
        else:
            dgs[j] = _DGS(gs[j], gs[j - 1])

        bflow[j] = _BFLOW(i[j], dgs[j])
        dro[j] = _DRO(watsur[j], i[j])
        sro[j] = _SRO(precip[j], PF)
        tro[j] = _TRO(bflow[j], dro[j], sro[j])
        flow[j] = _FLOW(tro[j], AREA, ndays[j])

    # results
    if report.lower() == "full":
        results = np.stack(
            (
                precip,
                nrain,
                ndays,
                ep,
                epm,
                ratepm,
                deltae,
                ea,
                pea,
                sms,
                smc,
                ss,
                watsur,
                i,
                cal0,
                calgs,
                gs,
                dgs,
                bflow,
                dro,
                sro,
                tro,
                flow,
            ),
            axis=1,
        )
        columns_name = [
            "PRECIP",
            "NRAIN",
            "NDAYS",
            "EP",
            "EPM",
            "RATEPM",
            "DELTAE",
            "EA",
            "PEA",
            "SMS",
            "SMC",
            "SS",
            "WATSUR",
            "I",
            "CAL0",
            "CALGS",
            "GS",
            "DGS",
            "BFLOW",
            "DRO",
            "SRO",
            "TRO",
            "FLOW",
        ]
    elif report.lower() == "partial":
        results = np.stack(
            (precip, nrain, ndays, ep, ea, sms, ss, gs, tro, flow), axis=1
        )
        columns_name = [
            "PRECIP",
            "NRAIN",
            "NDAYS",
            "EP",
            "EA",
            "SMS",
            "SS",
            "GS",
            "TRO",
            "FLOW",
        ]
    elif report.lower() == "tro":
        results = tro
        columns_name = ["TRO"]
    elif report.lower() == "flow":
        results = flow
        columns_name = ["FLOW"]
    else:
        raise ValueError(
            str(report) + " not identified. " + "Use full / partial / tro / flow."
        )

    if as_df:
        return pd.DataFrame(data=results, index=data.index, columns=columns_name)
    return results

"""
This module provides functions for reading and 
    manipulating hydrological data from an Excel workbook.

The functions in this module allow you to 
    extract data from specific sheets in the workbook, 
    filter the data by year and station, 
    and return the data as a pandas DataFrame or a list of DataFrames.

manual:
    https://gist.github.com/taruma/6d48b3ec9d601019c15fb5833ae03730

Functions:
- read_workbook(file_path, station_names=None, ignore_prefix="_", return_as_dataframe=True): 
    Read data from an Excel workbook and return it as a dictionary or a pandas DataFrame.
- _melt_to_year_vector(dataframe: pd.DataFrame, year: int) -> np.ndarray:
    Melt a pandas DataFrame to a 1D numpy array for a specific year.
- _generate_date_range_for_year(year) -> pd.DatetimeIndex:
    Return DateTimeIndex object for one year.
- _create_yearly_dataframe(dataframe: pd.DataFrame, year: int, station_name: str) -> pd.DataFrame:
    Create a DataFrame for one year.
- _extract_data_from_sheet(
    dataframe: pd.DataFrame, station: str, return_as_dataframe: bool = True
    ) -> Union[pd.DataFrame, List[pd.DataFrame]]:
        Extracts data from a sheet in the given dataframe and returns it 
        as a dataframe or a list of dataframes.

"""

from calendar import isleap
from typing import List, Union
import pandas as pd
import numpy as np
from hidrokit.contrib.taruma.utils import deprecated


def _melt_to_year_vector(dataframe: pd.DataFrame, year: int) -> np.ndarray:
    """
    Melt a pandas DataFrame to a 1D numpy array for a specific year.

    Args:
        dataframe: The pandas DataFrame to melt.
        year: The year to consider when melting the DataFrame.

    Returns:
        A 1D numpy array representing the melted DataFrame for the specified year.
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("dataframe must be a pandas DataFrame.")
    if not isinstance(year, int):
        raise ValueError("year must be an integer.")

    _drop = [59, 60, 61, 123, 185, 278, 340]
    _drop_leap = [60, 61, 123, 185, 278, 340]

    melted_data = dataframe.melt().drop("variable", axis=1)
    if isleap(year):
        return melted_data["value"].drop(_drop_leap).values
    return melted_data["value"].drop(_drop).values


def _generate_date_range_for_year(year):
    """Return DateTimeIndex object for one year.

    Args:
        year (int): The year for which to generate the date range.

    Returns:
        pd.DatetimeIndex: A DateTimeIndex object representing the date range for the specified year.
    """
    start_date = pd.Timestamp(year, 1, 1)
    end_date = pd.Timestamp(year + 1, 1, 1)
    return pd.date_range(start_date, end_date, inclusive="left")


def _create_yearly_dataframe(
    dataframe: pd.DataFrame, year: int, station_name: str
) -> pd.DataFrame:
    """
    Create a DataFrame for one year.

    Parameters:
        df (DataFrame): The original DataFrame.
        year (int): The year to filter the DataFrame.
        station_name (str): The name of the station.

    Returns:
        DataFrame: A new DataFrame with data for the specified year and station.
    """
    return pd.DataFrame(
        data=_melt_to_year_vector(dataframe, year),
        index=_generate_date_range_for_year(year),
        columns=[station_name],
    )


def _extract_data_from_sheet(
    dataframe: pd.DataFrame, station: str, return_as_dataframe: bool = True
) -> Union[pd.DataFrame, List[pd.DataFrame]]:
    """
    Extracts data from a sheet in the given dataframe and returns it
        as a dataframe or a list of dataframes.

    Parameters:
        dataframe (pd.DataFrame): The dataframe containing the sheet data.
        station (str): The name of the station.
        return_as_dataframe (bool, optional): Whether to return the data
            as a single dataframe or a list of dataframes. Defaults to True.

    Returns:
        Union[pd.DataFrame, List[pd.DataFrame]]:
            The extracted data as a dataframe or a list of dataframes.
    """
    total_years = int(dataframe.iloc[0, 1])

    yearly_dataframes = []
    for i in range(2, total_years * 33, 33):
        current_year = int(dataframe.iloc[i, 1])
        yearly_data = dataframe.iloc[i : i + 31, 4:16]
        yearly_dataframe = _create_yearly_dataframe(yearly_data, current_year, station)
        yearly_dataframes.append(yearly_dataframe)

    if return_as_dataframe:
        return pd.concat(yearly_dataframes, sort=True)

    return yearly_dataframes


def read_workbook(
    file_path, station_names=None, ignore_prefix="_", return_as_dataframe=True
):
    """
    Read data from an Excel workbook.

    Parameters:
        file_path (str): The path to the Excel workbook file.
        station_names (list or str, optional): The names of the sheets to read. 
            If not provided, all sheets will be read.
        ignore_prefix (str, optional): The prefix used to ignore sheets. Default is '_'.
        return_as_dataframe (bool, optional): Whether to return the data as a pandas DataFrame. 
            Default is True.

    Returns:
        dict or pandas.DataFrame: A dictionary containing the data from each sheet, 
            with sheet names as keys. If `return_as_dataframe` is True, 
            a pandas DataFrame is returned instead.

    """

    excel_file = pd.ExcelFile(file_path)

    station_data = {}
    all_sheet_names = excel_file.sheet_names
    if station_names is None:
        station_names = []
        for sheet_name in all_sheet_names:
            if not sheet_name.startswith(ignore_prefix):
                station_names.append(sheet_name)
    else:
        station_names = (
            [station_names] if isinstance(station_names, str) else station_names
        )

    for station_name in station_names:
        dataframe = excel_file.parse(sheet_name=station_name, header=None)
        station_data[station_name] = _extract_data_from_sheet(dataframe, station_name)

    if return_as_dataframe:
        return pd.concat(station_data.values(), sort=True, axis=1)

    return station_data


## Backward Compatibility (0.3.x - 0.4.x)


@deprecated("_melt_to_year_vector")
def _melt_to_array(*args, **kwargs):
    return _melt_to_year_vector(*args, **kwargs)


@deprecated("_generate_date_range_for_year")
def _index_daily(*args, **kwargs):
    return _generate_date_range_for_year(*args, **kwargs)


@deprecated("_create_yearly_dataframe")
def _yearly_df(*args, **kwargs):
    return _create_yearly_dataframe(*args, **kwargs)


@deprecated("_extract_data_from_sheet")
def _data_from_sheet(*args, **kwargs):
    return _extract_data_from_sheet(*args, **kwargs)

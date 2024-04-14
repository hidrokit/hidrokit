"""manual:
https://gist.github.com/taruma/05dab67fac8313a94134ac02d0398897
"""

from calendar import monthrange

# ref: https://www.reddit.com/r/learnpython/comments/485h1p/
from collections.abc import Sequence
import pandas as pd
import numpy as np
from hidrokit.contrib.taruma import hk43
from hidrokit.contrib.taruma.utils import deprecated


def _index_hourly(year, freq="60min"):
    """
    Create a DatetimeIndex with specific year or [year_start, year_end].

    Parameters:
        year (int or tuple): The year or range of years to create the index for.
            If an int is provided, the index will be created for that specific year.
            If a tuple is provided, the index will be created for the range of years
            specified by the tuple (inclusive).
        freq (str, optional): The frequency of the index. Defaults to "60min".

    Returns:
        pd.DatetimeIndex: The generated DatetimeIndex.

    """
    if isinstance(year, Sequence):
        year_start, year_end = year
    else:
        year_start, year_end = year, year

    period = f"{year_start}0101 00:00,{year_end}1231 23:00".split(",")
    return pd.date_range(*period, freq=freq)


def _melt_to_array(dataframe):
    """
    Convert a DataFrame to a 1-dimensional array by melting it and extracting the 'value' column.

    Parameters:
        df (pandas.DataFrame): The DataFrame to be converted.

    Returns:
        numpy.ndarray: A 1-dimensional array containing the values 
            from the 'value' column of the melted DataFrame.
    """
    return dataframe.melt().drop("variable", axis=1)["value"].values


def _get_array_in_month(dataframe, year, month):
    """
    Get an array of data for a specific year and month from a dataframe.

    Parameters:
        dataframe (pandas.DataFrame): The input dataframe.
        year (int): The year.
        month (int): The month.

    Returns:
        numpy.ndarray: The array of data for the specified year and month.
    """
    n_days = monthrange(year, month)[1]
    mask_month = slice(None, n_days)
    df_month = dataframe.iloc[mask_month, :].T
    return _melt_to_array(df_month)


def _get_array_in_year(df, year):
    """
    Get an array of data for a specific year from a DataFrame.

    Parameters:
        - df (pandas.DataFrame): The DataFrame containing the data.
        - year (int): The year for which the data is to be extracted.

    Returns:
        - numpy.ndarray: The array of data for the specified year.
    """
    n_rows, _ = df.shape

    # configuration (view the excel)
    n_month = 1  # number of row to monthID
    n_gap = 2  # number of row between month pivot table
    n_lines = 31 + n_gap  # number of row each month

    data = []
    for row in range(1, n_rows, n_lines):
        mask_start = row + n_month
        mask_end = row + n_lines

        month = df.iloc[mask_start, 1]
        mask_row = slice(mask_start, mask_end)

        df_month = df.iloc[mask_row, 4:]
        array_month = _get_array_in_month(df_month, year, month)
        data.append(array_month)

    return np.hstack(data)


def get_info(file, config_sheet=None):
    """
    Retrieves information from an Excel file.

    Args:
        file (str): The path to the Excel file.
        config_sheet (str, optional): The name of the sheet to read from. 
            If not provided, the first sheet will be used.

    Returns:
        dict: A dictionary containing the information retrieved from the Excel file. 
            The keys are the lowercase values from the first column, 
            and the values are the corresponding values from the second column.
    """
    excel = pd.ExcelFile(file)
    first_sheet = excel.sheet_names[0]
    config_sheet = first_sheet if config_sheet is None else config_sheet

    df = pd.read_excel(excel, sheet_name=config_sheet, header=None, usecols="A:B")
    info = {}

    for index, _ in df.iterrows():
        key = df.iloc[index, 0].lower()
        value = df.iloc[index, 1]
        info[str(key)] = value

    return info

@deprecated("get_info")
def _get_info(file, config_sheet=None):
    return get_info(file, config_sheet=config_sheet)


def read_excel_hourly(file, station=None):
    """
    Read hourly data from an Excel file.

    Parameters:
        file (str): The path to the Excel file.
        station (str, optional): The name of the station. Defaults to None.

    Returns:
        pandas.DataFrame: A DataFrame containing the hourly data.

    """
    excel = pd.ExcelFile(file)

    # CONFIG
    years = hk43.extract_years_from_excel(excel)
    station = "NA" if station is None else station

    # READ DATA
    data = []
    for year in years:
        sheet = pd.read_excel(
            excel, sheet_name=str(year), header=None, nrows=396, usecols="A:AB"
        )
        array = _get_array_in_year(sheet, year)
        df_year = pd.DataFrame(data=array, columns=[station], index=_index_hourly(year))
        data.append(df_year)

    return pd.concat(data, axis=0)

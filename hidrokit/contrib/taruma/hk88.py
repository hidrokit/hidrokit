"""manual:
https://gist.github.com/taruma/6d48b3ec9d601019c15fb5833ae03730
"""

from calendar import isleap
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


def _data_from_sheet(df, station_name, as_df=True):
    """Read dataset from single sheet as dataframe (or list of dataframe)"""
    n_years = int(df.iloc[0, 1])

    frames = []
    for i in range(2, n_years * 33, 33):
        year = int(df.iloc[i, 1])
        pivot = df.iloc[i : i + 31, 4:16]
        data = _create_yearly_dataframe(pivot, year, station_name)
        frames.append(data)

    if as_df:
        return pd.concat(frames, sort=True)
    else:
        return frames


def read_workbook(io, stations=None, ignore_str="_", as_df=True):
    """Read dataset from workbook"""
    excel = pd.ExcelFile(io)

    data = {}
    sheet_names = excel.sheet_names
    if stations is None:
        stations = []
        for sheet in sheet_names:
            if not sheet.startswith(ignore_str):
                stations.append(sheet)
    else:
        stations = [stations] if isinstance(stations, str) else stations

    for station in stations:
        df = excel.parse(sheet_name=station, header=None)
        data[station] = _data_from_sheet(df, station)

    if as_df:
        return pd.concat(data.values(), sort=True, axis=1)
    else:
        return data


## Backward Compatibility


@deprecated('_melt_to_year_vector')
def _melt_to_array(*args, **kwargs):
    return _melt_to_year_vector(*args, **kwargs)

@deprecated('_generate_date_range_for_year')
def _index_daily(*args, **kwargs):
    return _generate_date_range_for_year(*args, **kwargs)

@deprecated('_create_yearly_dataframe')
def _yearly_df(*args, **kwargs):
    return _create_yearly_dataframe(*args, **kwargs)

# _data_from_sheet
# read_workbook

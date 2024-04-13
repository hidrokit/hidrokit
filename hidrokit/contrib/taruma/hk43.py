"""manual:
https://gist.github.com/taruma/a9dd4ea61db2526853b99600909e9c50"""

from calendar import isleap
from collections import defaultdict
from pathlib import Path
from typing import List
import pandas as pd
import numpy as np
from hidrokit.contrib.taruma.utils import deprecated

DROP_INDICES = [59, 60, 61, 123, 185, 278, 340]
DROP_INDICES_LEAP = [60, 61, 123, 185, 278, 340]


def _extract_years_from_excel(file_path: str) -> List[int]:
    """
    Get a list of years from an Excel file.

    Parameters:
        file_path (str): The path to the Excel file.

    Returns:
        List[int]: A sorted list of years found in the Excel file.
    """
    excel = pd.ExcelFile(file_path)
    years = []
    for sheet in excel.sheet_names:
        if sheet.isdigit():
            years.append(int(sheet))
    return sorted(years)


def _get_pivot_from_excel(excel_file: str, year: int, data_format: str) -> pd.DataFrame:
    """
    Get a pivot table from an Excel file.

    Parameters:
        excel_file (str): The path to the Excel file.
        year (int): The year of the data to retrieve.
        data_format (str): The format of the data to retrieve.

    Returns:
        pandas.DataFrame: The pivot table containing the data.

    Raises:
        ValueError: If the data format is unknown.
    """
    # Map data formats to parameters
    formats = {
        "uma.debit": ("AN:AY", 16, 47),
        "uma.hujan": ("B:M", 19, 50),
    }

    if data_format not in formats:
        raise ValueError(f"Unknown data format: {data_format}")

    usecols, start_row, end_row = formats[data_format]

    # Read the Excel data
    df = pd.read_excel(excel_file, sheet_name=str(year), header=None, usecols=usecols)

    # Return the pivot
    return df.iloc[start_row:end_row, :]


def _get_data_for_year(file_path, year, data_format):
    """
    Get data for a specific year from a file and return it as a single vector numpy array.

    Parameters:
        file_path (str): The path to the file.
        year (int): The year for which to retrieve the data.
        data_format (str): The format of the data.

    Returns:
        numpy.ndarray: The data for the specified year.

    Raises:
        ValueError: If the year is not a positive integer.
        IOError: If the file cannot be read.
    """
    if not isinstance(year, int) or year < 0:
        raise ValueError("Year must be a positive integer.")

    try:
        pivot_table = _get_pivot_from_excel(
            file_path, str(year), data_format=data_format
        )
    except Exception as e:
        raise IOError("Could not read file: " + str(e)) from e

    reshaped_data = pivot_table.melt().drop("variable", axis=1)

    if isleap(year):
        return reshaped_data["value"].drop(DROP_INDICES_LEAP).values
    return reshaped_data["value"].drop(DROP_INDICES).values


def _get_data_allyear(io, fmt, aslist=False):
    list_years = _extract_years_from_excel(io)

    data_each_year = []

    for year in list_years:
        data = _get_data_for_year(io, year=year, data_format=fmt)
        data_each_year.append(data)

    if aslist:
        return data_each_year

    return np.hstack(data_each_year)


def _get_invalid(array, check):
    dict_invalid = defaultdict(list)
    for index, element in enumerate(array):
        try:
            check(element)
            if np.isnan(check(element)):
                dict_invalid["NaN"] += [index]
        except ValueError:
            dict_invalid[element] += [index]

    return dict(dict_invalid)


def _have_invalid(array, check):
    return bool(_get_invalid(array, check=check))


def _check_invalid(array, check=float):
    if _have_invalid(array, check=check):
        return _get_invalid(array, check=check)
    return None


def read_folder(dataset_path, pattern, fmt, prefix="", invalid=False):
    dataset_path = Path(dataset_path)
    total_files = len(list(dataset_path.glob(pattern)))
    print(f"Found {total_files} file(s)")

    data_allstation = {}
    data_invalid = {}

    for counter, file in enumerate(dataset_path.glob(pattern)):
        print(f":: {counter + 1:^4}:\t{file.name:s}")
        station_name = prefix + "_".join(file.stem.split("_")[1:-2])
        data_each_station = _get_data_allyear(file, fmt=fmt)
        data_allstation[station_name] = data_each_station
        if invalid:
            data_invalid[station_name] = _check_invalid(data_each_station)

    if invalid:
        return data_allstation, data_invalid
    return data_allstation


@deprecated("_extract_years_from_excel")
def _get_years(io: str) -> List[int]:
    return _extract_years_from_excel(io)


@deprecated("_get_pivot_from_excel")
def _get_pivot(io, year, fmt):
    return _get_pivot_from_excel(io, year, fmt)


@deprecated("_get_data_for_year")
def _get_data_oneyear(io, year, fmt):
    return _get_data_for_year(io, year, fmt)

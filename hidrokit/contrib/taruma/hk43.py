"""manual:
https://gist.github.com/taruma/a9dd4ea61db2526853b99600909e9c50"""

from calendar import isleap
from collections import defaultdict
from pathlib import Path
from typing import List
import pandas as pd
import numpy as np
from hidrokit.contrib.taruma.utils import deprecated


def _extract_years_from_excel(io: str) -> List[int]:
    """
    Get a list of years from an Excel file.

    Args:
        io (str): The path to the Excel file.

    Returns:
        List[int]: A sorted list of years found in the Excel file.
    """
    excel = pd.ExcelFile(io)
    years = []
    for sheet in excel.sheet_names:
        if sheet.isdigit():
            years.append(int(sheet))
    return sorted(years)


def _get_pivot_from_excel(excel_file, year, data_format):
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


def _get_data_oneyear(io, year, fmt):
    _drop = [59, 60, 61, 123, 185, 278, 340]
    _drop_leap = [60, 61, 123, 185, 278, 340]

    pivot_table = _get_pivot_from_excel(io, str(year), data_format=fmt)
    data = pivot_table.melt().drop("variable", axis=1)
    if isleap(year):
        return data["value"].drop(_drop_leap).values
    return data["value"].drop(_drop).values


def _get_data_allyear(io, fmt, aslist=False):
    list_years = _extract_years_from_excel(io)

    data_each_year = []

    for year in list_years:
        data = _get_data_oneyear(io, year=year, fmt=fmt)
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

"""
hk43: pamarayan_excel_data_extraction
This module provides functions for reading and 
    extracting data from Excel files in a specific format.

Manual:
https://gist.github.com/taruma/a9dd4ea61db2526853b99600909e9c50

Functions:
- _extract_years_from_excel(file_path: str) -> List[int]:
    Get a list of years from an Excel file.

- _get_pivot_from_excel(excel_file: str, year: int, data_format: str) -> pd.DataFrame:
    Get a pivot table from an Excel file.

- _get_data_for_year(file_path: str, year: int, data_format: str) -> np.ndarray:
    Get data for a specific year from a file and return it as a single vector numpy array.

- _get_data_all_year(
    file_path: Union[str, Path], data_format: str, return_as_list: bool = False
    ) -> Union[List[np.ndarray], np.ndarray]:
        Get data for all years from a given file.

- _get_invalid_elements_indices(
    num_array: Any, validation_func: Callable[[Any], Any]
    ) -> Dict[str, List[int]]:
        Returns a dictionary containing the indices of invalid elements in the given `num_array`.

- have_invalid(array: List[Any], validation_func: Callable[[Any], Any]) -> bool:
    Check if the given array has any invalid elements based on the provided validation function.

- _check_invalid(array, validation_func=float):
    Check if there are any invalid elements in the array.

- read_folder(
    dataset_path: str,
    filename_pattern: str,
    data_format: str,
    station_name_prefix: str = "",
    check_for_invalid_data: bool = False
) -> Union[Dict[str, np.ndarray], Dict[str, np.ndarray], Dict[str, List[int]]]:
    Read files from a folder and extract data for each station.

Deprecated Functions:
- _get_years(io: str) -> List[int]:
    Deprecated. Use _extract_years_from_excel instead.

- _get_pivot(io, year, fmt):
    Deprecated. Use _get_pivot_from_excel instead.

- _get_data_oneyear(io, year, fmt):
    Deprecated. Use _get_data_for_year instead.

- _get_data_allyear(*args, **kwargs):
    Deprecated. Use _get_data_all_year instead.

- _get_invalid(*args, **kwargs):
    Deprecated. Use _get_invalid_elements_indices instead.

- _have_invalid(*args, **kwargs):
    Deprecated. Use have_invalid instead.
"""

from calendar import isleap
from collections import defaultdict
from pathlib import Path
from typing import Callable, Any, Dict, Union, List
import logging
import pandas as pd
import numpy as np
from hidrokit.contrib.taruma.utils import deprecated

DROP_INDICES = [59, 60, 61, 123, 185, 278, 340]
DROP_INDICES_LEAP = [60, 61, 123, 185, 278, 340]


def extract_years_from_excel(file_path: str) -> List[int]:
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


def _get_data_for_year(file_path: str, year: int, data_format: str) -> np.ndarray:
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


def _get_data_all_year(
    file_path: Union[str, Path], data_format: str, return_as_list: bool = False
) -> Union[List[np.ndarray], np.ndarray]:
    """
    Get data for all years from a given file.

    Args:
        file_path (Union[str, Path]): The path to the file.
        data_format (str): The format of the data.
        return_as_list (bool, optional): Whether to return the data as a list of arrays.
            Defaults to False.

    Returns:
        Union[List[np.ndarray], np.ndarray]: The data for all years.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"No such file or directory: '{file_path}'")

    list_years = extract_years_from_excel(file_path)

    data_each_year = []

    for year in list_years:
        data = _get_data_for_year(file_path, year=year, data_format=data_format)
        data_each_year.append(data)

    if return_as_list:
        return data_each_year

    return np.hstack(data_each_year)


def _get_invalid_elements_indices(
    num_array: Any, validation_func: Callable[[Any], Any]
) -> Dict[str, List[int]]:
    """
    Returns a dictionary containing the indices of invalid elements in the given `num_array`.

    Parameters:
    - num_array (array-like): The array containing the elements to be validated.
    - validation_func (function): The validation function to be applied to each element.

    Returns:
    - invalid_element_indices (defaultdict):
        A defaultdict object containing the indices of invalid elements.
        The keys of the dictionary represent the type of invalidity,
        such as "NaN" for elements that are NaN, and
        the values are lists of indices corresponding to each type of invalidity.
    """
    invalid_element_indices: Dict[str, List[int]] = defaultdict(list)
    for index, element in enumerate(num_array):
        try:
            result = validation_func(element)
            if np.isnan(result):
                invalid_element_indices["NaN"].append(index)
        except ValueError:
            invalid_element_indices[str(element)].append(index)

    return invalid_element_indices


def have_invalid(array: List[Any], validation_func: Callable[[Any], Any]) -> bool:
    """
    Check if the given array has any invalid elements based on the provided validation function.

    Args:
        array (list): The array to check for invalid elements.
        validation_func (function): The validation function used
            to determine if an element is invalid.

    Returns:
        bool: True if the array has any invalid elements, False otherwise.
    """
    return bool(_get_invalid_elements_indices(array, validation_func=validation_func))


def _check_invalid(array, validation_func=float):
    """
    Check if there are any invalid elements in the array.

    Parameters:
        array (iterable): The array to check.
        validation_func (callable): The validation function to use.

    Returns:
        dict or None: A dictionary with the indices of invalid elements,
            or None if there are no invalid elements.
    """
    invalid_elements_indices = _get_invalid_elements_indices(
        array, validation_func=validation_func
    )
    return invalid_elements_indices if invalid_elements_indices is not None else None


def read_folder(
    dataset_path: str,
    filename_pattern: str,
    data_format: str,
    station_name_prefix: str = "",
    check_for_invalid_data: bool = False,
) -> Union[Dict[str, np.ndarray], Dict[str, np.ndarray], Dict[str, List[int]]]:
    """
    Read files from a folder and extract data for each station.

    Args:
        dataset_path (str): The path to the dataset folder.
        filename_pattern (str): The pattern to match the filenames.
        data_format (str): The format of the data in the files.
        station_name_prefix (str, optional): The prefix to add to the station names.
            Defaults to "".
        check_for_invalid_data (bool, optional): Whether to check for invalid data.
            Defaults to False.

    Returns:
        dict: A dictionary containing the extracted data for each station.
            If `check_for_invalid_data` is True,
            it also returns a dictionary of invalid data for each station.
    """
    dataset_path = Path(dataset_path)
    all_files = list(dataset_path.rglob(filename_pattern))
    total_files = len(all_files)

    if total_files == 0:
        logging.warning("No files found that match the pattern %s", filename_pattern)
        return {}

    logging.info("Found %d file(s)", total_files)

    all_station_data = {}
    invalid_data = {}

    for counter, file in enumerate(dataset_path.glob(filename_pattern)):
        logging.info(":: %4d:\t%s", counter, file.name)
        station_name = station_name_prefix + "_".join(file.stem.split("_")[1:-2])
        each_station_data = _get_data_all_year(file, data_format=data_format)
        all_station_data[station_name] = each_station_data
        if check_for_invalid_data:
            invalid_data[station_name] = _check_invalid(each_station_data)

    if check_for_invalid_data:
        return all_station_data, invalid_data
    return all_station_data


@deprecated("_extract_years_from_excel")
def _get_years(io: str) -> List[int]:
    return extract_years_from_excel(io)


@deprecated("_get_pivot_from_excel")
def _get_pivot(io, year, fmt):
    return _get_pivot_from_excel(io, year, fmt)


@deprecated("_get_data_for_year")
def _get_data_oneyear(io, year, fmt):
    return _get_data_for_year(io, year, fmt)


@deprecated("_get_data_all_year")
def _get_data_allyear(*args, **kwargs):
    return _get_data_all_year(*args, **kwargs)


@deprecated("_get_invalid_elements_indices")
def _get_invalid(array, check):
    return _get_invalid_elements_indices(array, validation_func=check)


@deprecated("have_invalid")
def _have_invalid(array, check):
    return have_invalid(array, validation_func=check)

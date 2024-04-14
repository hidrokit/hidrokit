"""
hk99: thiessen.py

This module provides functions for calculating Thiessen weights 
    and applying the Thiessen polygon method 
    to calculate the weighted average of values in a dataset.

For more information, refer to the manual: 
    https://gist.github.com/taruma/8dd920bee9fa95cf6eba39cc9d694953
"""

from typing import Union
import numpy as np
import pandas as pd


def thiessen_weight(area: dict) -> dict:
    """
    Calculate the Thiessen weights for a given area.

    Parameters:
        area (dict): A dictionary containing the areas as keys and their corresponding values.

    Returns:
        dict: A dictionary containing the Thiessen weights,
            where the keys are the areas and the values are the weights.
    """
    area_val = list(area.values())
    area_percent = area_val / np.sum(area_val)
    key = list(area.keys())
    return dict(zip(key, area_percent))


def apply_thiessen(
    dataset: pd.DataFrame, area: dict, columns: list = None, as_df: bool = True
) -> Union[pd.DataFrame, np.ndarray]:
    """
    Applies the Thiessen polygon method to calculate the weighted average of values in a dataset.

    Parameters:
        dataset (pandas.DataFrame): The dataset containing the values to be weighted.
        area (dict): A dictionary mapping column names to their respective Thiessen polygon areas.
        columns (list, optional): A list of column names to be included in the calculation.
            If None, all columns in the dataset will be used. Default is None.
        as_df (bool, optional): Specifies whether to return the result as a pandas DataFrame.
            If True, a DataFrame will be returned.
            If False, a numpy array will be returned.
            Default is True.

    Returns:
        pandas.DataFrame or numpy.ndarray: The weighted average values.
            If `as_df` is True, a DataFrame will be returned with a single column named 'thiessen'.
            If `as_df` is False, a numpy array will be returned.

    """
    weight = thiessen_weight(area)

    columns = columns if columns is not None else dataset.columns

    val = []
    for col in columns:
        val.append(dataset[col].values * weight[col])

    np_val = np.stack(val, axis=1)

    if as_df:
        return pd.DataFrame(
            data=np_val.sum(axis=1), index=dataset.index, columns=["thiessen"]
        )
    else:
        return np_val.sum(axis=1)

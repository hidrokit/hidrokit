"""This module provides functions for creating tensor arrays from pandas DataFrames.

This module contains the following functions:
- `_columns_index`: Get the index of columns in a dataframe.
- `_get_y`: Get the target variable(s) from the input array.
- `_get_x_tensor`: Generate a tensor of input features for a given array.
- `tensor_array`: Convert a pandas DataFrame into 
    a tensor array for input to a machine learning model.

For more information, refer to the manual: 
    https://gist.github.com/taruma/50460ebfaab5a30c41e7f1a1ac0853e2
"""

import numpy as np


def _columns_index(dataframe, columns):
    """
    Get the index of columns in a dataframe.

    Args:
        dataframe (pandas.DataFrame): The dataframe to search for column indices.
        columns (list): A list of column names.

    Returns:
        list: A list of column indices corresponding to the input column names.
    """
    column_names = dataframe.columns
    column_indices = []

    for column in columns:
        column_indices.append(column_names.get_loc(column))
    return column_indices


def _get_y(array, timesteps, columns_index):
    """
    Get the target variable(s) from the input array.

    Parameters:
        array (ndarray): The input array.
        timesteps (int): The number of timesteps to skip from the beginning of the array.
        columns_index (list): The indices of the columns to extract.

    Returns:
        ndarray: The target variable(s) extracted from the input array.
    """
    y = []
    for col in columns_index:
        y.append(array[timesteps:, col])

    if len(columns_index) == 1:
        return y[0]
    return np.stack(y, axis=1)


def _get_x_tensor(array, timesteps, columns_index):
    """
    Generate a tensor of input features for a given array.

    Parameters:
        array (numpy.ndarray): The input array.
        timesteps (int): The number of timesteps to consider for each feature.
        columns_index (list): The indices of the columns to include in the tensor.

    Returns:
        numpy.ndarray: The tensor of input features.

    """
    X = []  # pylint: disable=invalid-name
    rows, _ = array.shape

    for col in columns_index:
        array_each_column = []
        for row in range(timesteps, rows):
            array_each_column.append(array[row - timesteps : row, col])
        X.append(array_each_column)

    return np.stack(X, axis=2)


def tensor_array(
    dataframe,
    timesteps,
    X_columns=None,  # pylint: disable=invalid-name
    y_out=False,
    y_columns=None,
):
    """
    Convert a pandas DataFrame into a tensor array for input to a machine learning model.

    Args:
        dataframe (pandas.DataFrame): The input DataFrame containing the data.
        timesteps (int): The number of timesteps to consider for each sample.
        X_columns (list, optional): The list of column names to be used as input features.
            If None, all columns will be used. Defaults to None.
        y_out (bool, optional): Whether to include the output labels in the tensor array.
            Defaults to False.
        y_columns (list, optional): The list of column names to be used as output labels.
            Only applicable if y_out is True. Defaults to None.

    Returns:
        numpy.ndarray: The tensor array representing the input data.

        If y_out is True, the function also returns:
        numpy.ndarray: The tensor array representing the output labels.
    """

    _, n_cols = dataframe.shape
    array = dataframe.values

    # pylint: disable=invalid-name
    # X array
    if X_columns is None:
        X_index = range(n_cols)
    else:
        X_index = _columns_index(dataframe, X_columns)

    X = _get_x_tensor(array, timesteps=timesteps, columns_index=X_index)

    # y array
    if y_out is True:
        if y_columns is None:
            y_index = [n_cols - 1]
        else:
            y_index = _columns_index(dataframe, y_columns)

        y = _get_y(array, timesteps=timesteps, columns_index=y_index)
        return X, y

    return X

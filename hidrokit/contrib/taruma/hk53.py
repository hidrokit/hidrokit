"""This module provides functions for creating tensor arrays from pandas DataFrames.

Functions:
- tensor_array(dataframe, timesteps, X_columns=None, y_out=False, y_columns=None): 
  Creates a tensor array from the given DataFrame.
  Args:
    - dataframe: The input DataFrame.
    - timesteps: The number of time steps to consider for each sample.
    - X_columns: A list of column names to be used as input features. If None, all columns will be used.
    - y_out: A boolean indicating whether to include the output labels in the tensor array. Default is False.
    - y_columns: A list of column names to be used as output labels. Only applicable if y_out is True.
  Returns:
    - If y_out is False, returns the tensor array X.
    - If y_out is True, returns a tuple (X, y) where X is the tensor array and y is the output labels array.
"""

import numpy as np


def _columns_index(dataframe, columns):
    """Get the column indices for the given column names in the DataFrame."""
    columns_name = dataframe.columns
    columns_index = []

    for column in columns:
        columns_index.append(columns_name.get_loc(column))
    return columns_index


def _get_y(array, timesteps, columns_index):
    """Get the output labels array from the input array."""
    y = []
    for col in columns_index:
        y.append(array[timesteps:, col])

    if len(columns_index) == 1:
        return y[0]
    else:
        return np.stack(y, axis=1)


def _get_x_tensor(array, timesteps, columns_index):
    """Get the tensor array X from the input array."""
    X = []
    rows, _ = array.shape

    for col in columns_index:
        array_each_column = []
        for row in range(timesteps, rows):
            array_each_column.append(array[row - timesteps:row, col])
        X.append(array_each_column)

    return np.stack(X, axis=2)


def tensor_array(
    dataframe, timesteps, X_columns=None, y_out=False, y_columns=None
):
    """Create a tensor array from the given DataFrame.

    Args:
        dataframe: The input DataFrame.
        timesteps: The number of time steps to consider for each sample.
        X_columns: A list of column names to be used as input features. If None, all columns will be used.
        y_out: A boolean indicating whether to include the output labels in the tensor array. Default is False.
        y_columns: A list of column names to be used as output labels. Only applicable if y_out is True.

    Returns:
        If y_out is False, returns the tensor array X.
        If y_out is True, returns a tuple (X, y) where X is the tensor array and y is the output labels array.
    """
    _, n_cols = dataframe.shape
    array = dataframe.values

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

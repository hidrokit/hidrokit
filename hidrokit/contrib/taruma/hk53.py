"""manual:
https://gist.github.com/taruma/50460ebfaab5a30c41e7f1a1ac0853e2"""

import numpy as np


def _columns_index(dataframe, columns):
    columns_name = dataframe.columns
    columns_index = []

    for column in columns:
        columns_index.append(columns_name.get_loc(column))
    return columns_index


def _get_y(array, timesteps, columns_index):
    y = []
    for col in columns_index:
        y.append(array[timesteps:, col])

    if len(columns_index) == 1:
        return y[0]
    else:
        return np.stack(y, axis=1)


def _get_x_tensor(array, timesteps, columns_index):
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

"""Manipulation timestep dataframe."""

import numpy as np
import pandas as pd


def _timestep_single(array, index=0, timesteps=2, keep_first=True):
    """Add timesteps array for single column array.

    Parameters
    ----------
    array : array
        Single column two-dimensional array.
    index : int, optional
        Index column, by default 0
    timesteps : int, optional
        Number of timesteps, by default 2
    keep_first : bool, optional
        Include original array if set True, by default True

    Returns
    -------
    array
        Return 2D array with timesteps.
    """
    if array.ndim == 1:
        array = array.reshape(-1, 1)

    x = []

    for i in range(timesteps + 1):
        start = timesteps - i
        end = -i if i > 0 else None
        x.append(array[start:end, index])

    if not keep_first:
        x.pop(-1)

    return np.array(x).transpose()


def _timestep_multi(array, index=None, timesteps=2, keep_first=True):
    """Add timesteps array for multiple column array.

    Parameters
    ----------
    array : array
        Multiple numeric column two-dimensional array.
    index : list of int, optional
        List of columns index, by default None
    timesteps : int, optional
        Number of timesteps, by default 2
    keep_first : bool, optional
        Include original column if set True, by default True

    Returns
    -------
    array
        Return 2D array with timesteps.
    """
    _, col = array.shape
    col = range(col)
    x = []

    for c in col:
        arr = array[:, c].reshape(-1, 1)
        if index is None:
            x.append(_timestep_single(arr, timesteps=timesteps,
                                      keep_first=keep_first))
        elif c in index:
            x.append(_timestep_single(arr, timesteps=timesteps,
                                      keep_first=keep_first))
        else:
            x.append(arr[timesteps:])

    return np.concatenate(x, axis=1)


def timestep_table(dataframe,
                   columns=None,
                   timesteps=2, keep_first=True):
    """Generate timesteps directly from DataFrame.

    Parameters
    ----------
    dataframe : DataFrame
        Dataframe consist of numeric-column only
    columns : list of str, optional
        List of columns name to generate, by default None
    timesteps : int, optional
        Number of timesteps, by default 2
    keep_first : bool, optional
        Column _tmin0 will be included if set True, by default True

    Returns
    -------
    DataFrame
        DataFrame with additional timesteps columns.
    """
    # dataframe parameter
    columns_name = list(dataframe.columns)
    new_index = dataframe.index[timesteps:]

    # Generate new column name
    new_columns_name = []
    for column in columns_name:
        if columns is None:
            for i in range(timesteps + 1):
                new_columns_name.append(f"{column}_tmin{i}")
        elif column in columns:
            for i in range(timesteps + 1):
                new_columns_name.append(f"{column}_tmin{i}")
        else:
            new_columns_name.append(column)
    if keep_first is False:
        for column in new_columns_name:
            if column.endswith("_tmin0"):
                new_columns_name.remove(column)

    # Convert name columns to index
    index_columns = []
    if columns is not None:
        for column in columns:
            index_columns.append(columns_name.index(column))
    else:
        index_columns = None

    # Generate Dataframe column with timesteps
    columns_values = dataframe.values
    columns_values = _timestep_multi(
        columns_values,
        index=index_columns,
        keep_first=keep_first,
        timesteps=timesteps
    )
    timestep_dataframe = pd.DataFrame(
        data=columns_values,
        index=new_index,
        columns=new_columns_name
    )

    return timestep_dataframe

# -*- coding: utf-8 -*-
"""Module for deep learning.

Use this module for preparation data in modeling of deep learning.
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_dataset(dataset, ncols=3, nrows=5, figsize=None):
    """Plot all numeric column in one figure with datetime index.

    Parameters
    ----------
    dataset : :class:`pandas.DataFrame`
        Dataframe consist of numeric column only.
    ncols : int, optional
        Number of column subplots, by default 3
    nrows : int, optional
        Number of row subplots, by default 5
    figsize : tuple of int, optional
        Figure size, by default None
    """
    fig, axes = plt.subplots(ncols=ncols, nrows=nrows, figsize=figsize,
                             sharex=True)

    idx = 0
    column_name = dataset.columns

    for row in range(nrows):
        for col in range(ncols):

            if ncols == 1:
                position = (row)
            else:
                position = (row, col)

            dataset[column_name[idx]].plot(ax=axes[position])
            axes[position].set_title(column_name[idx],
                                     loc='right' if ncols == 1 else 'center')

            if idx < len(column_name) - 1:
                idx += 1
            else:
                break

    plt.tight_layout()
    return fig, axes

# Fungsi untuk membuat kolom tambahan sesuai timesteps


def single_column_timesteps(array, index_col=0, n_timesteps=2, first_col=True):
    """Add timesteps array for single column array.

    Parameters
    ----------
    array : :class:`np.ndarray`
        Single column two-dimensional array.
    index_col : int, optional
        Index column, by default 0
    n_timesteps : int, optional
        Number of timesteps, by default 2
    first_col : bool, optional
        Include original array if set True, by default True

    Returns
    -------
    :class:`np.ndarray`
        Return 2D array with timesteps.
    """
    if array.ndim == 1:
        array = array.reshape(-1, 1)

    x = []
    for i in range(n_timesteps + 1):
        start = n_timesteps - i
        end = -i if i > 0 else None
        x.append(array[start:end, index_col])
    if not first_col:
        x.pop(-1)

    return np.array(x).transpose()


def multi_column_timesteps(array, idx_col=None, n_timesteps=2, first_col=True):
    """Add timesteps array for multiple column array.

    Parameters
    ----------
    array : :class:`np.ndarray`
        Multiple numeric column two-dimensional array.
    idx_col : list of int, optional
        List of columns index, by default None
    n_timesteps : int, optional
        Number of timesteps, by default 2
    first_col : bool, optional
        Include original column if set True, by default True

    Returns
    -------
    :class:`np.ndarray`
        Return 2D array with timesteps.
    """
    _, col = array.shape
    col = range(col)

    x = []

    for c in col:
        arr = array[:, c].reshape(-1, 1)
        if idx_col is None:
            x.append(single_column_timesteps(arr, n_timesteps=n_timesteps,
                                             first_col=first_col))
        elif c in idx_col:
            x.append(single_column_timesteps(arr, n_timesteps=n_timesteps,
                                             first_col=first_col))
        else:
            x.append(arr[n_timesteps:])

    return np.concatenate(x, axis=1)


def table_timesteps(dataset,
                    columns_timesteps=None,
                    n_timesteps=2, first_col=True):
    """Generate timesteps dataframe directly from :class:`pandas.DataFrame`.

    Parameters
    ----------
    dataset : :class:`pandas.DataFrame`
        Dataframe consist of numeric-column only. 
    columns_timesteps : list of str, optional
        List of columns name to generate, by default None
    n_timesteps : int, optional
        Number of timesteps, by default 2
    first_col : bool, optional
        Column _tmin0 will be included if set True, by default True

    Returns
    -------
    :class:`pandas.DataFrame`
        Dataframe with additional timesteps columns.
    """
    # Dataset parameter
    columns_name = list(dataset.columns)
    new_index = dataset.index[n_timesteps:]

    # Generate new column name
    new_columns_name = []
    for column in columns_name:
        if columns_timesteps is None:
            for i in range(n_timesteps + 1):
                new_columns_name.append(f"{column}_tmin{i}")
        elif column in columns_timesteps:
            for i in range(n_timesteps + 1):
                new_columns_name.append(f"{column}_tmin{i}")
        else:
            new_columns_name.append(column)
    if first_col is False:
        for column in new_columns_name:
            if column.endswith("_tmin0"):
                new_columns_name.remove(column)

    # Convert name columns to index
    index_columns_timesteps = []
    if columns_timesteps is not None:
        for column in columns_timesteps:
            index_columns_timesteps.append(columns_name.index(column))
    else:
        index_columns_timesteps = None

    # Generate Dataframe column with timesteps
    columns_values = dataset.values
    columns_timesteps_values = multi_column_timesteps(columns_values,
                                                      idx_col=index_columns_timesteps,
                                                      first_col=first_col,
                                                      n_timesteps=n_timesteps)

    df_timesteps = pd.DataFrame(data=columns_timesteps_values,
                                index=new_index,
                                columns=new_columns_name)

    return df_timesteps

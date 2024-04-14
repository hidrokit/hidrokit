"""
This module provides functions for calculating summary statistics on datasets.

Functions:
- summary_station(dataset, column, ufunc, ufunc_col, n_days='MS'): 
    Calculate summary statistics for a given dataset and column.
- summary_all(dataset, ufunc, ufunc_col, columns=None, n_days='MS', verbose=False): 
    Calculate summary statistics for multiple columns in a dataset.

For more details, refer to the manual: 
https://gist.github.com/taruma/aca7f90c8fbb0034587809883d0d9e92
"""

import numpy as np
import pandas as pd


# pylint: disable=too-many-arguments
def summary_station(dataset, column, ufunc, ufunc_col, n_days="MS"):
    """
    Calculate summary statistics for a given dataset and column.

    Parameters:
    - dataset (pd.DataFrame): The dataset containing the data.
    - column (str): The column name for which summary statistics are calculated.
    - ufunc (tuple or list): The aggregation functions to apply to the data.
    - ufunc_col (tuple or list): The names for the aggregated columns.
    - n_days (str, optional): The frequency at which to summarize the data.
        Default is 'MS' (monthly start).

    Returns:
    - summary (pd.DataFrame): The summarized data with aggregated values.

    Raises:
    - ValueError: If the lengths of ufunc and ufunc_col are not matched.

    """
    grouped = [dataset.index.year, dataset.index.month]

    ufunc = ufunc if isinstance(ufunc, (list, tuple)) else (ufunc,)
    ufunc_col = ufunc_col if isinstance(ufunc_col, (list, tuple)) else (ufunc_col,)

    if len(ufunc) != len(ufunc_col):
        raise ValueError("length ufunc and ufunc_col are not matched.")

    if n_days.endswith("D") or n_days.endswith("MS") or n_days.endswith("M"):
        ix_month = []
        val_month = []
        for _, x in dataset[column].groupby(by=grouped):
            each_month = x.groupby(pd.Grouper(freq=n_days)).agg(ufunc)
            val_month.append(each_month.values)
            ix_month.append(each_month.index.to_numpy())
        return pd.DataFrame(
            data=np.vstack(val_month),
            index=np.hstack(ix_month),
            columns=pd.MultiIndex.from_product([[column], ufunc_col]),
        ).rename_axis("DATE")

    summary = dataset[[column]].resample(n_days).agg(ufunc)
    summary.columns = pd.MultiIndex.from_product([[column], ufunc_col])
    return summary


def summary_all(dataset, ufunc, ufunc_col, columns=None, n_days="MS", verbose=False):
    """
    Calculate summary statistics for multiple columns in a dataset.

    Parameters:
    - dataset (pandas.DataFrame): The dataset containing the columns
        to calculate summary statistics for.
    - ufunc (callable): The function to apply for calculating the summary statistics.
    - ufunc_col (str): The column in the dataset to apply the ufunc function on.
    - columns (list or str, optional): The columns in the dataset
        to calculate summary statistics for.
        If not provided, all columns in the dataset will be used.
    - n_days (str, optional): The frequency of the summary statistics.
        Defaults to 'MS' (monthly start).
    - verbose (bool, optional): Whether to print the processing status for each column.
        Defaults to False.

    Returns:
    - pandas.DataFrame: A DataFrame containing the summary statistics for each column.

    """
    res = []

    columns = columns if columns is not None else list(dataset.columns)
    columns = columns if isinstance(columns, (list, tuple)) else [columns]

    for column in columns:
        if verbose:
            print("PROCESSING:", column)
        res.append(summary_station(dataset, column, ufunc, ufunc_col, n_days=n_days))
    return pd.concat(res, axis=1)

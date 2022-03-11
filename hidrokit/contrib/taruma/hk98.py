"""manual:
https://gist.github.com/taruma/aca7f90c8fbb0034587809883d0d9e92"""

import numpy as np
import pandas as pd


def summary_station(dataset, column, ufunc, ufunc_col, n_days='MS'):
    grouped = [dataset.index.year, dataset.index.month]

    ufunc = ufunc if isinstance(ufunc, (list, tuple)) else (ufunc,)
    ufunc_col = (ufunc_col
                 if isinstance(ufunc_col, (list, tuple)) else (ufunc_col,))

    if len(ufunc) != len(ufunc_col):
        raise ValueError('length ufunc and ufunc_col are not matched.')

    ix_month = []
    val_month = []
    for _, x in dataset[column].groupby(by=grouped):
        each_month = x.groupby(pd.Grouper(freq=n_days)).agg(ufunc)
        val_month.append(each_month.values)
        ix_month += each_month.index
    return pd.DataFrame(
        data=np.vstack(val_month), index=ix_month,
        columns=pd.MultiIndex.from_product([[column], ufunc_col])
    )


def summary_all(dataset, ufunc, ufunc_col, columns=None, n_days='MS', verbose=False):
    res = []

    columns = columns if columns is not None else list(dataset.columns)
    columns = columns if isinstance(columns, (list, tuple)) else [columns]

    for column in columns:
        if verbose:
            print('PROCESSING:', column)
        res.append(
            summary_station(dataset, column, ufunc, ufunc_col, n_days=n_days)
        )
    return pd.concat(res, axis=1)

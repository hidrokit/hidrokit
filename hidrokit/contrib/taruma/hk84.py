"""manual:
https://gist.github.com/taruma/cad07f29ffc025ba9e7801e752be3444
"""

from hidrokit.contrib.taruma import hk73
import pandas as pd


def _time_grouped(
    df, index_grouped, col, date_fmt='%Y-%m-%d', hour_fmt='%H:%M'
):
    """Return index_grouped as (list of date, list of hour)"""
    date = []
    hour = []
    for item in index_grouped:
        date_val = df.iloc[[item[0]], col].index.strftime(date_fmt).to_list()
        hour_val = df.iloc[[item[0]], col].index.strftime(hour_fmt).to_list()
        date.append(date_val)
        hour.append(hour_val)
    return date, hour


def _value_grouped(df, index_grouped, col):
    """Return index_grouped as list of value list"""
    value = []
    for item in index_grouped:
        value_val = df.iloc[item, col].to_list()
        value.append(value_val)
    return value


def _dict_grouped(date_list, hour_list, value_list, start=0):
    """Join three list and return as dictionary"""
    item_list = enumerate(zip(date_list, hour_list, value_list), start=start)
    return {
        i: date + hour + value for i, (date, hour, value) in item_list
    }


def summary_hourly(df, column, n_hours=24,
                   text_date=['date', 'hour'], as_df=True,
                   date_fmt='%Y-%m-%d', hour_fmt='%H:%M'):
    col = df.columns.get_loc(column)
    nrows, _ = df.shape
    results = {}

    for i in range(0, nrows, n_hours):
        sub_df = df.iloc[i:i + n_hours]
        ix_array = hk73._get_index1D(~sub_df.iloc[:, col].isna().values)
        ix_grouped = hk73._group_as_list(ix_array)
        date, hour = _time_grouped(sub_df, ix_grouped,
                                   col, date_fmt=date_fmt, hour_fmt=hour_fmt)
        value = _value_grouped(sub_df, ix_grouped, col)
        each_hours = _dict_grouped(date, hour, value, start=i)
        results.update(each_hours)

    if as_df:
        columns_name = text_date + [i for i in range(1, n_hours + 1)]
        df_results = pd.DataFrame.from_dict(
            results, orient='index', columns=columns_name
        )
        return df_results
    else:
        return results

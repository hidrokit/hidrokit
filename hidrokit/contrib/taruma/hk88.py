from calendar import isleap
import pandas as pd


def _melt_to_array(df, year):
    # ref: hidrokit.contrib.taruma.hk43
    _drop = [59, 60, 61, 123, 185, 278, 340]
    _drop_leap = [60, 61, 123, 185, 278, 340]

    data = df.melt().drop('variable', axis=1)
    if isleap(year):
        return data['value'].drop(_drop_leap).values
    else:
        return data['value'].drop(_drop).values


def _index_daily(year):
    year_range = '{}0101 {}0101'.format(year, year + 1).split()
    return pd.date_range(*year_range, closed='left')


def _yearly_df(df, year, station_name):
    return pd.DataFrame(
        data=_melt_to_array(df, year),
        index=_index_daily(year),
        columns=[station_name]
    )


def _data_from_sheet(df, station_name, as_df=True):
    n_years = int(df.iloc[0, 1])

    frames = []

    for i in range(2, n_years * 33, 33):
        year = int(df.iloc[i, 1])
        pivot = df.iloc[i:i + 31, 4:16]
        data = _yearly_df(pivot, year, station_name)
        frames.append(data)

    if as_df:
        return pd.concat(frames)
    else:
        return frames


def read_workbook(io, stations, as_df=True):
    excel = pd.ExcelFile(io)

    data = []
    for station in stations:
        df = pd.read_excel(excel, sheet_name=station, header=None)
        data.append(_data_from_sheet(df, station))

    if as_df:
        return pd.concat(data, sort=True)
    else:
        return data

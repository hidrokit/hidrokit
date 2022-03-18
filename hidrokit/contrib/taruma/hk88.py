"""manual:
https://gist.github.com/taruma/6d48b3ec9d601019c15fb5833ae03730
"""

from calendar import isleap
import pandas as pd


def _melt_to_array(df, year):
    """Melt dataframe to 1D array one year"""
    # ref: hidrokit.contrib.taruma.hk43
    _drop = [59, 60, 61, 123, 185, 278, 340]
    _drop_leap = [60, 61, 123, 185, 278, 340]

    data = df.melt().drop('variable', axis=1)
    if isleap(year):
        return data['value'].drop(_drop_leap).values
    else:
        return data['value'].drop(_drop).values


def _index_daily(year):
    """Return DateTimeIndex object for one year"""
    year_range = '{}0101 {}0101'.format(year, year + 1).split()
    return pd.date_range(*year_range, closed='left')


def _yearly_df(df, year, station_name):
    """Create dataframe for one year"""
    return pd.DataFrame(
        data=_melt_to_array(df, year),
        index=_index_daily(year),
        columns=[station_name]
    )


def _data_from_sheet(df, station_name, as_df=True):
    """Read dataset from single sheet as dataframe (or list of dataframe)"""
    n_years = int(df.iloc[0, 1])

    frames = []
    for i in range(2, n_years * 33, 33):
        year = int(df.iloc[i, 1])
        pivot = df.iloc[i:i + 31, 4:16]
        data = _yearly_df(pivot, year, station_name)
        frames.append(data)

    if as_df:
        return pd.concat(frames, sort=True)
    else:
        return frames


def read_workbook(io, stations=None, ignore_str='_', as_df=True):
    """Read dataset from workbook"""
    excel = pd.ExcelFile(io)

    data = {}
    sheet_names = excel.sheet_names
    if stations is None:
        stations = []
        for sheet in sheet_names:
            if not sheet.startswith(ignore_str):
                stations.append(sheet)
    else:
        stations = [stations] if isinstance(stations, str) else stations

    for station in stations:
        df = excel.parse(sheet_name=station, header=None)
        data[station] = _data_from_sheet(df, station)

    if as_df:
        return pd.concat(data.values(), sort=True, axis=1)
    else:
        return data

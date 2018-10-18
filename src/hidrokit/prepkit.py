# New format 20181007

import pandas as pd
import pathlib
from calendar import monthrange

## CHECK AND WARNING


## STAGE SCANNING
def sc_getyear(file, format='phderi'):
    file = pathlib.Path(file)
    if format == 'phderi':
        return int(file.stem.split()[0])
    return None

def sc_getname(file, format='phderi', ixn=-2):
    file = pathlib.Path(file)
    if format == 'phderi':
        return ''.join(file.stem.split()[ixn:])
    return None

## STAGE GET


def get_indextable(rawxl, format='phderi'):
    targetdict = {'phderi': ['Jan', 'Feb'], 
                  'pdderi': ['JAN', 'FEB']}
    target, check = targetdict[format]
    index = []
    for col in rawxl:
        if rawxl[col].astype(str).str.contains('^'+target+'$').sum():
            index.append(col)
            break
    col = index[0]
    row_target = rawxl[col] == target
    
    index.append(rawxl[col][row_target].index.values.astype(int)[0])
    kolom, baris = index
    if rawxl.iloc[baris, kolom + 1] == check:
        rawxl.iloc[baris + 1:baris + 32, kolom:kolom + 12]
    else:
        raise Exception(f'Format tidak sesuai dengan {format}')

    return index


def get_rawdf(singlefile, format='phderi'):
    singlefile = pathlib.Path(singlefile)
    if format == 'phderi' or format == 'pdderi':
        xl = pd.read_excel(singlefile, sheet_name=0, header=None)
        kolom, baris = get_indextable(xl, format)
        rawdf = xl.iloc[baris + 1:baris + 32, kolom:kolom + 12]
        return rawdf


## STAGE TRANSFORM


def tf_emptydf(year):
    """ Creating emptydf with index of date in single year """
    start, end = map(pd.Timestamp, f'{year}0101 {year}1231'.split())

    df = pd.DataFrame()
    df['date'] = pd.date_range(start, end)
    df.set_index('date', inplace=True)
    return df


def tf_column(tabledf, year):
    """ Return in single column """
    month = 1
    data_column = []

    for col in tabledf:
        days = monthrange(year, month)[1]
        end = 31 if (days == 31) else (days - 31)
        data_column += tabledf[col][:end].tolist()
        month += 1

    return data_column


def tf_rawdf(rawdf, year, name='ch'):
    """ Transform rawdf to single column dataframe"""
    maindf = tf_emptydf(year)
    data = tf_column(rawdf, year)
    maindf[name] = data
    return maindf


## STAGE JOIN
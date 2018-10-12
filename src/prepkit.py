# New format 20181007

import pandas as pd
import numpy as np
import pathlib
from calendar import monthrange

## CHECK AND WARNING

## STAGE SCANNING
def sc_getyear(file, format='phderi'):
    file = pathlib.Path(file)
    if format == 'phderi':
        return int(file.stem.split()[0])


## STAGE GET

def get_indextable(rawxl, format='phderi'):
    targetdict = {'phderi':['Jan','Feb'],
                  'pdderi':['JAN','FEB']}
    index = []
    targetformat = targetdict[format]
    target, check = targetformat
    index = []
    for col in rawxl:
        if rawxl[col].astype(str).str.contains(target).sum():
            index.append(col)
            
    index.append(rawxl[index[0]][rawxl[index[0]]==target].index.values.astype(int)[0])
    kolom,baris = index
    if rawxl.iloc[baris, kolom + 1] == check:
        rawxl.iloc[baris+1:baris+32, kolom:kolom+12]
        pass
    else:
        raise Exception(f'Format tidak sesuai dengan {format}')

    return index 

def get_rawdf(singlefile, format='phderi'):
    singlefile = pathlib.Path(singlefile)
    if format == 'phderi' or format == 'pdderi':
        xl = pd.read_excel(singlefile,
                           sheet_name=0,
                           header=None)
        kolom, baris = get_indextable(xl, format)
        rawdf = xl.iloc[baris+1:baris+32,kolom:kolom+12]
        return rawdf



## STAGE TRANSFORM


def tf_emptydf(year):
    """ Creating emptydf with index of date in single year """
    start, end = map(pd.Timestamp, f'{year}0101 {year}1231'.split())

    df = pd.DataFrame()
    df['date'] = pd.date_range(start, end)
    df.set_index('date',inplace=True)
    return df


def tf_column(tabledf, year):
    """ Return in single column """
    #    if len(rawdf.columns) != 12:
    #        print('Table is not compatible, only have {} column'
    #              .format(rawdf.shape[1]))
    #        return

    month = 1
    data_column = []

    for col in tabledf:
        days = monthrange(year, month)[1]
        
        end = 31 if (days == 31) else (days - 31)

        data_column += tabledf[col][:end].tolist()
        month += 1

    return data_column

def tf_rawdf(rawdf, year, name='ch'):
    maindf = tf_emptydf(year)
    data = tf_column(rawdf, year)
    maindf[name] = data
    return maindf

## STAGE JOIN
    

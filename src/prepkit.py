# New format 20181007

import pandas as pd
import numpy as np
import pathlib
from datetime import datetime, timedelta
from calendar import monthrange

## CHECK AND WARNING

## STAGE SCANNING

## STAGE GET

## STAGE TRANSFORM


def tf_emptydf(year):
    """ Creating emptydf with index of date in single year """
    start, end = map(pd.Timestamp, f'{year}0101 {year}1231'.split())

    df = pd.DataFrame()
    df['date'] = pd.date_range(start, end)
    df.set_index('date',inplace=True)
    return df


def tf_column(rawdf, year):
    #    if len(rawdf.columns) != 12:
    #        print('Table is not compatible, only have {} column'
    #              .format(rawdf.shape[1]))
    #        return

    month = 1
    data_column = []

    for col in rawdf:
        days = monthrange(year, month)[1]
        
        end = 31 if (days == 31) else (days - 31)

    data_column += rawdf[col][:end].tolist()
    month += 1

    pass


def tf_rawdf(rawdf, year, name='CH'):
    df = tf_emptydf(year)
    data = tf_column(rawdf, year)

    pass


## STAGE JOIN
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:58:18 2018

@author: tarum
"""

import pandas as pd
import os
import pathlib
from datetime import datetime, timedelta
from calendar import monthrange


def create_df_rain(year):
    """ Creating dataframe with index of date in single year """

    df = pd.DataFrame()
    start_date = datetime(year, month=1, day=1)
    end_date = datetime(year, month=12, day=monthrange(year, 12)[1])
    step = timedelta(days=1)
    list_of_date = []

    while start_date <= end_date:
        list_of_date.append(start_date)
        start_date += step

    df['date'] = list_of_date
    df.set_index('date', inplace=True)
    return df


def get_list_rain(tabledf, year):
    """ transform table to single column """
    month = 1
    list_of_rain = []

    for col in tabledf:
        days_in_month = monthrange(year, month)[1]

        if not (days_in_month == 31):
            end_month = days_in_month - 31
        else:
            end_month = 31

        list_of_rain += tabledf[col][:end_month].tolist()
        month += 1

    return list_of_rain


def transform_raw_data(raw_data, year, name='ch'):
    """ Transforming raw data to dataframe for analysis"""

    main_df = create_df_rain(year)
    # Cleaning Raw Data
    data_rain = get_list_rain(raw_data, year)

    main_df[name] = data_rain
    return main_df


def check_name_sheet(string):
    string = string.replace(' ', '')
    if string.isdigit() and (len(string) == 4):
        return int(string)
    else:
        print(f'sheet name is = {string}, set to 2002\n'
              'please change sheet name to 4 digit year')
        return 2002


def read_data_excel(file, name="ch"):
    """ Reading data single excel file to dataframe"""
    try:
        xl = pd.read_excel(file, sheet_name=None, index_col=0)
        list_year = []
        for sheet in xl.keys():
            year = check_name_sheet(sheet)
            df_year = transform_raw_data(xl[sheet], year, name=name)
            list_year.append(df_year)
        df_main = pd.concat(list_year)
        return df_main
    except Exception as e:
        print(e)


def multi_read_data(dirpath):
    pathdir = pathlib.Path(dirpath)
    list_stat = []
    for file in pathdir.rglob('*.xls*'):
        df = read_data_excel(file, name=file.stem)
        list_stat.append(df)
    df_main = pd.concat(list_stat, axis=1, sort=False)
    return df_main


if __name__ == "__main__":
    #    a = pathlib.Path('./testdata/xls/spam_singlesheet.xlsx')
    #    df = read_data_excel(a, name='kota 1')
    #    print(df)

    #    MULTI FILE
    #    pathdir = pathlib.Path('./testdata/xls/multi_station')
    #    list_stat = []
    #    for file in pathdir.rglob('*.xls*'):
    #        df = read_data_excel(file, name=file.stem)
    #        list_stat.append(df)
    #    print(list_stat)
    df_main = multi_read_data('./testdata/xls/multi_station')
    print(df_main.shape)

#    pass
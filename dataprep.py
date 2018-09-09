# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:58:18 2018

@author: tarum
"""

import pandas as pd
from datetime import datetime, timedelta
from calendar import monthrange

def read_data_excel(file):
    """ Reading data excel to dataframe"""
    try:
        data = pd.read_excel(file, index_col=0)
        return data
    except Exception as e:
        print(e)
#    pass
        
def create_df_rain(year):
    df = pd.DataFrame()
    start_date = datetime(year, month=1, day=1)
    end_date = datetime(year, month=12, day=monthrange(year, 12)[1])
    step = timedelta(days=1)
    list_of_date = []
    
    while start_date <= end_date:
#        print(start_date)
        list_of_date.append(start_date)
        start_date += step   
    
    df['date'] = list_of_date
    df.set_index('date', inplace=True)
    return df

def get_list_rain(raw_data, year):
    month = 1
    list_of_rain = []
    for col in raw_data:

        days_in_month = monthrange(year, month)[1]
        
        if not(days_in_month == 31):
            end_month = days_in_month - 31
        else:
            end_month = 31
            
        list_of_rain += raw_data[col][:end_month].tolist()
        month += 1
    
    return list_of_rain

def transform_raw_data(raw_data, year):
    """ Transforming raw data to dataframe for analysis"""
    
    main_df = create_df_rain(year)
    # Cleaning Raw Data
    data_rain = get_list_rain(raw_data, year)
    
    main_df['ch'] = data_rain
    return main_df

def main():
    year = 2002
    file = "xls\\example.xlsx"
    raw_data = read_data_excel(file)
    print(raw_data)
    df_rain = transform_raw_data(raw_data, year=year)
    print(df_rain)    

if __name__ == "__main__":
    year = 2002
    file = "xls\\example.xlsx"
    raw_data = read_data_excel(file)
    df_rain = transform_raw_data(raw_data, year=year)
    df_rain
#    main()
# -*- coding: utf-8 -*-

#import pandas as pd
#import numpy as np
#
#data_num = pd.read_csv('loss_num.csv', index_col=0)
#data_date = pd.read_csv('loss_date.csv', index_col=0, parse_dates=[0])
#
#a = pd.DataFrame()
#a['date'] = pd.date_range('20000101', '20010101')
#
#for col in ['num1', 'num2', 'num3', 'num4']:
#    ran = np.random.rand(len(a)) * 100
#    ran[ran < 20] = np.nan
#    a[col] = ran
#
#a_date = a.set_index('date')
#a_num = a.drop('date', axis=1)
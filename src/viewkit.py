# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 14:55:04 2018

@author: tarum
"""

def in_pivot(df=None, col=None):
#    df['month'] = df.index.month
#    df['day'] = df.index.day
    df = df.assign(month=df.index.month, day=df.index.day)
    return df.pivot(values=col, columns='month', index='day')

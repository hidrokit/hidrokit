# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 14:55:04 2018

@author: tarum
"""

def in_pivot(df=None, col=None):
    col = df.columns[0] if not col else col
    return df.assign(month=df.index.month, day=df.index.day
              ).pivot(values=col, columns='month', index='day')
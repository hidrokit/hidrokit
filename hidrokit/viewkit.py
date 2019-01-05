# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 14:55:04 2018

@author: tarum
"""

monthDict = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun',
             7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
monthDictID = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'Mei', 6:'Jun',
               7:'Jul', 8:'Agu', 9:'Sep', 10:'Okt', 11:'Nov', 12:'Des'}

def in_pivot(df=None, col=None, month_fmt=None):
    col = df.columns[0] if not col else col
    
    viewdf = df.assign(month=df.index.month, day=df.index.day
              ).pivot(values=col, columns='month', index='day')
    
    if month_fmt:
        if month_fmt.lower() == 'id':
            viewdf.columns = viewdf.columns.map(monthDictID)
        elif month_fmt.lower() == 'en':
            viewdf.columns = viewdf.columns.map(monthDict)
        
    
    return viewdf
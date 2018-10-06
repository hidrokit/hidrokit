# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 08:45:55 2018

@author: tarum
"""

from pathlib import Path

a = './testdata/xls/multi_station'
p = Path(a).absolute()

for i in p.rglob('*.xls*'):
    print(i.stem)
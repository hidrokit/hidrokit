# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:01:13 2018

@author: tarum
"""

import pandas as pd
import pathlib

pathfile = pathlib.Path(__file__)
metadata_file = pathfile.parent / 'metadata_station.csv'
#metadata_file = pathlib.Path('metadata_station.csv')

metadata_station = pd.read_csv(metadata_file, index_col=0)
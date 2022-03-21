"""manual:
https://gist.github.com/taruma/96c321175ecac3e51350ef4c94f3d7d4"""

import numpy as np
import pandas as pd

# ref: https://stackoverflow.com/q/29612705/4886384
def upsampling(df, freq='D', fill_method='ffill', 
               use_inter=False, inter_method='linear', inter_keys={}, 
               reindex=False):
    start = df.index.min() - pd.DateOffset(day=1)
    end = df.index.max() - pd.DateOffset(day=31)
    date = pd.date_range(start, end, freq=freq)

    newdf = df.reindex(date)

    if reindex:
        return newdf

    if use_inter:
        return newdf.interpolate(method=inter_method, **inter_keys)
    else:
        return newdf.fillna(method=fill_method)
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

## Fungsi membuat grafik
def plot_dataset(dataset, ncols=3, nrows=5, figsize=None):
    fig, axes = plt.subplots(ncols=ncols, nrows=nrows, figsize=figsize,
                             sharex=True)
    
    idx = 0
    column_name = dataset.columns
    
    for row in range(nrows):
        for col in range(ncols):
            
            if ncols == 1:
                position = (row)
            else:
                position = (row, col)
            
            dataset[column_name[idx]].plot(ax=axes[position])
            axes[position].set_title(column_name[idx],
                                     loc='right' if ncols==1 else 'center')
            
            if idx < len(column_name)-1:
                idx += 1
            else:
                break
    
    plt.tight_layout()
    return fig, axes

## Fungsi untuk membuat kolom tambahan sesuai timesteps
def single_column_timesteps(array, index_col=0, n_timesteps=2, first_col=True):
    if array.ndim == 1:
        array = array.reshape(-1,1)
    
    x = []
    for i in range(n_timesteps+1):
        start = n_timesteps - i
        end = -i if i > 0 else None
        x.append(array[start:end, index_col])
    if not first_col:
        x.pop(-1)
        
    return np.array(x).transpose()

def multi_column_timesteps(array, n_timesteps=2, first_col=True):
    row, col = array.shape
    x = []
    
    for c in range(col):
        arr = array[:, c].reshape(-1,1)
        x.append(single_column_timesteps(arr, n_timesteps=n_timesteps,
                                         first_col=first_col))
    
    return np.concatenate(x, axis=1)
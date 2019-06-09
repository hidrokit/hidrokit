# -*- coding: utf-8 -*-

def dict_null_data(dataset, date=True, date_format='%Y/%m/%d'):
    loss_row = {}
    
    for column in dataset.columns:
        
        if date:
            idx_null = dataset[dataset[column].isnull()].index.strftime(date_format).values.tolist()
        else:
            idx_null = dataset[dataset[column].isnull()].index.values.tolist()

        loss_row[column] = idx_null
    return loss_row
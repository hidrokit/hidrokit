"""manual:
https://gist.github.com/taruma/8dd920bee9fa95cf6eba39cc9d694953"""

import numpy as np
import pandas as pd


def thiessen_weight(area):
    area_val = list(area.values())
    area_percent = area_val / np.sum(area_val)
    key = list(area.keys())
    return dict(zip(key, area_percent))


def apply_thiessen(dataset, area, columns=None, as_df=True):
    weight = thiessen_weight(area)

    columns = columns if columns is not None else dataset.columns

    val = []
    for col in columns:
        val.append(dataset[col].values * weight[col])

    np_val = np.stack(val, axis=1)

    if as_df:
        return pd.DataFrame(
            data=np_val.sum(axis=1), index=dataset.index, columns=['thiessen']
        )
    else:
        return np_val.sum(axis=1)

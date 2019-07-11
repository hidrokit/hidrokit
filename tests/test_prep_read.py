"""Test for .prep.read module
"""

from hidrokit.prep import read
import numpy as np
import pandas as pd

A = pd.DataFrame(
    data=[
        [1, 3, 4, np.nan, 2, np.nan],
        [np.nan, 2, 3, np.nan, 1, 4],
        [2, np.nan, 1, 3, 4, np.nan]
    ],
    columns=['A', 'B', 'C', 'D', 'E', 'F']
)

A_date = A.set_index(pd.date_range("20190617", "20190619"))

res_A_number = {'A': [1], 'B': [2], 'C': [], 'D': [0, 1], 'E': [], 'F': [0, 2]}
res_A_date = {'A': ['0618'], 'B': ['0619'], 'C': [],
              'D': ['0617', '0618'], 'E': [], 'F': ['0617', '0619']}


def test_read_number():
    test = read.missing_row(A, date_index=False)
    assert test.items() == res_A_number.items()


def test_read_date():
    test = read.missing_row(A_date, date_format="%m%d")
    assert test.items() == res_A_date.items()

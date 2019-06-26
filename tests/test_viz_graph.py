"""Test for .viz.graph module
"""

import pandas as pd

from hidrokit.viz import graph

# ======
# Public
# ======


def test_subplots():
    data = pd.read_csv('tests/data/one_year_three_columns.csv',
                       index_col=0, parse_dates=True)
    _, ax = graph.subplots(data, ncols=1, nrows=3)

    assert ax.shape[0] == 3

    _, ax = graph.subplots(data, ncols=2, nrows=2)
    col, row = ax.shape

    assert col == 2
    assert row == 2

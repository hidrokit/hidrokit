"""Test for .viz.table module
"""

import numpy as np
import pandas as pd
from numpy.testing import assert_equal

from hidrokit.viz import table

# ======
# Public
# ======


def test_pivot():
    data = pd.read_csv('tests/data/one_year_three_columns.csv',
                       index_col=0, parse_dates=True)

    # Argument: None

    row_4 = np.array([81., 38., 41., 62., 5., 70.,
                      67., 27., 61., 5., 96., 84.])
    col_0 = np.array(
        [7., 17., 79., 48., 81., 26., 78., 71., 48., 32., 66., 93., 94.,
         98., 40., 46., 34., 21., 61., 62., 25., 98., 51., 83., 73., 54.,
         90., 61., 6., 64., 72.]
    )
    assert_equal(row_4, table.pivot(data).iloc[4, :].values)
    assert_equal(col_0, table.pivot(data).iloc[:, 0].values)

    # Argument: lang

    month_en = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_id = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun',
                'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']

    assert month_en == table.pivot(data, lang='en').columns.to_list()
    assert month_id == table.pivot(data, lang='id').columns.to_list()

    # Argument: columns

    b_row_15 = np.array(
        [22., 39., 23., 51., 74., 75., 83., 63., 56., 62., 14., 54.]
    )

    c_col_5_10 = np.array(
        [34., 40., 41., 69., 77., 98., 35., 89., 83., 31.]
    )

    assert_equal(
        b_row_15, table.pivot(data, column='sta_b').iloc[15, :].values
    )
    assert_equal(
        c_col_5_10, table.pivot(data, column='sta_c').iloc[:10, 5].values
    )

"""Test for .prep.excel module
"""

# =======
# PRIVATE
# =======
import numpy as np
import pandas as pd
from numpy.testing import assert_equal
from pandas.testing import assert_index_equal, assert_frame_equal

from hidrokit.prep import excel


def test__file_year():
    filepath = 'tests/data/excel/2006 HUJAN DISNEY LAND.xls'
    year = excel._file_year(filepath)

    assert year == 2006


def test__file_single_pivot():
    filepath = 'tests/data/excel/2006 HUJAN DISNEY LAND.xls'
    pivot = excel._file_single_pivot(filepath)
    pivot = pivot.replace('-', np.nan)

    nan = np.nan
    row_3 = np.array(
        [66.3, nan, 11.3, nan, nan, 13.2, nan, nan, nan, nan, nan,
         12.3]
    )

    assert_equal(
        row_3, pivot.iloc[3, :].values
    )


def test__dataframe_year():
    data = pd.read_csv('tests/data/one_year_one_column.csv',
                       index_col=0, parse_dates=True)

    data_test = excel._dataframe_year(2000)

    assert_index_equal(
        data.index, data_test.index
    )


def test__dataframe_data():
    filepath = 'tests/data/excel/2013 DUGAAIR.xls'
    pivot = excel._file_single_pivot(filepath, template='pdderi')
    pivot = pivot.replace('-', np.nan)

    pivot_list = excel._dataframe_data(pivot, 2013)
    assert pivot_list[0] == 1.33
    assert pivot_list[-1] == 1.20


def test__dataframe_table():
    filepath = 'tests/data/excel/2013 DUGAAIR.xls'
    pivot = excel._file_single_pivot(filepath, template='pdderi')
    dataframe = excel._dataframe_table(pivot, 2013, name='dugaair')

    result = pd.read_csv('tests/data/2013 DUGAAIR.csv',
                         index_col=0, parse_dates=True)
    assert_frame_equal(
        result, dataframe
    )

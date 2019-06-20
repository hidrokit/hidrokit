"""Module for reading BMKG's Microsoft Excel file. 

.. deprecated:: 0.2.0
   Use :py:mod:`prepkit` instead.

.. seealso::
   Module :py:mod:`prepkit`
"""

import pandas as pd
import pathlib

pathfile = pathlib.Path(__file__)
metadata_file = pathfile.parent / 'database' / 'bmkg_metadata_station.csv'
metadata_station = pd.read_csv(metadata_file, index_col=0)
metadata_last_update = "20181018"

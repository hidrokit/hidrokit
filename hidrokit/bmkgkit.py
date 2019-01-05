# bmkgkit contains database from bmkg online

import pandas as pd
import pathlib

pathfile = pathlib.Path(__file__)
metadata_file = pathfile.parent / 'database' / 'bmkg_metadata_station.csv'
metadata_station = pd.read_csv(metadata_file, index_col=0)
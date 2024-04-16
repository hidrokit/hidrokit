# Changelog
All significant changes to this project will be documented in this log. This documentation is only for changes to the Python package.

The writing is adapted from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for version numbering.

---
## Unreleased

---
## Released

### 2022-04-05 - 0.4.0

**Added**
- Added module `.contrib.taruma`:
  - #102 `hk102`: upsampling dataset.
  - #151 `hk151`: outlier test.
  - #158 `hk158`: statistical parameter calculation.
  - Distribution Goodness-of-Fit Test Module:
    - #140 `hk140`: Kolmogorov-Smirnov test.
    - #141 `hk141`: Chi-square test.
  - Frequency Analysis Module:
    - #124 `hk124`: 2-parameter log-normal distribution.
    - #126 `hk126`: Pearson Type III log distribution.
    - #127 `hk127`: Gumbel distribution.
    - #172 `hk172`: Normal distribution.
  - #179 CDF function `.calc_prob()` for each frequency analysis.
  - #194 `anfrek`: module containing a collection of frequency analysis functions.

**Fixed**
- #169 Fixed test function `test_prep_excel.test__dataframe_table()`.
- #115 Added `verbose=False` argument to module `.contrib.taruma.hk98`.
- #162 Updated function `.contrib.taruma.hk88.read_workbook()` to read all sheets without specifying station/sheet name.

**Changed**
- #162 The output of `as_df=False` argument in function `.contrib.taruma.hk88.read_workbook()` changed from a list to a dictionary.

### 2020-07-13 - 0.3.6

**Fixed**
- Fixed the `keep_first=False` argument in the `timeseries.timestep_table()` function.

### 2020-01-15 - 0.3.5

**Added**
- Added module `.contrib.taruma`:
  - `hk87`: calculation of dependable flow using flow duration curve.
  - `hk88`: extract daily rainfall dataset from excel.
  - `hk89`: NRECA model.
  - `hk90`: model calibration (NRECA/FJMOCK).
  - `hk99`: calculation of rainfall using Thiessen polygon method.
  - `hk98`: summary of time series dataset.
  - `hk96`: F.J. Mock model.
  - `hk102`: upsampling dataset.
  - `hk106`: evapotranspiration calculation.

### 2019-12-09 - 0.3.4

**Added**
- Added module `.contrib.taruma`:
  - `hk84`: summarizing rainfall data information.

### 2019-11-30 - 0.3.3

**Added**
- Added module `.contrib.taruma`:
  - `hk79`: extracting rainfall data information from excel.
- Added `makefile` for easier publishing.

**Changed**
- Fixed citation file (.cff).
- Fixed `hidrokit.__version__` invocation.
- Fixed lint, i.e., lines that are too long.
### 2019-10-15 - 0.3.2

**Added**
- Added subpackage `.contrib.taruma` with the following modules:
  - `.hk43`: convert pivot table to dataframe
  - `.hk53`: create table/tensor for LSTM deep learning modeling
  - `.hk73`: process files from bmkg
- Added subpackage `.contrib` for contributor-only code without CI checks.
- Added .cff file for citation and Zenodo reading.

**Changed**
- Changed the tag format from "v0.3.2" to "0.3.2" for automatic reading by Zenodo.

---
### 2019-07-26 - v0.2.1

**Changed**
- Added `template=` argument to `prep.timeseries.timestep_table` function.
- Changed f-string usage to `.format` for compatibility with Python 3.5.
- Changed codecov configuration.
- Changed travis-ci configuration. Added Python 3.5 check.

### 2019-07-11 - v0.2.0

**Added**
- Renamed modules and functions to be more readable and memorable.
- Divided the package into three main sections: preparation (`prep`), analysis (`analysis`), and visualization (`viz`). Renamed modules and functions to adhere to standard naming conventions for clarity and ease of use.
  - Modules for data reading and manipulation, such as `dlkit`, `datakit`, `prepkit`, are now under the `prep` module and renamed to `timeseries`, `read`, `excel`.
  - Modules for data visualization, such as `viewkit`, and plot functions from `dlkit`, are now under the `viz` module and renamed to `table` and `graph`.
  - Some function names have been changed to be more descriptive, such as `datakit.dict_null_data` to `prep.read.missing_row()`.
- Integrated with Travis CI, Codecov, Codacy.
- Testing using pytest with a target of 90% coverage.
- Released the [hidrokit] and [hidrokit-nb] websites, which include contribution guidelines and general project information.

**Fixed**
- Improved the documentation at [hidrokit.readthedocs.io] by dividing it into three pages: data preparation, data analysis, and data visualization.

**Removed**
- Removed the `bmkgkit` module, which has no replacement yet.
- The following modules have been removed/replaced and will no longer be used:
  - `dlkit`, `viewkit`, `bmkgkit`, `prepkit`, `datakit`.

---
### 2019-06-25 - v0.1.3

**Added**
- Technical documentation site at [readthedocs](https://hidrokit.rtfd.io).
- `docstring` for each method.

### 2019-06-10 - v0.1.2

**Added**
- Module `.datakit`.
- Function `.dlkit.table_timesteps()`.
- New argument in function `.dlkit.multi_column_timesteps()` to customize function `.dlkit.table_timesteps()`.

**Documentation - v0.1.2**
- Changed template for issues and PRs.
- Added changelog document.
- Moved notebooks to the repository [`hidrokit-nb`](https://github.com/taruma/hidrokit-nb).

### 2019-05-14 - v0.1.1

**Added**
- Module `.dlkit`.

### 2019-01-09 - v0.1.0

**Added**
- Converted `hidrokit` to a Python package.
- Distribution of `hidrokit` via PyPI.

**Documentation**
- Changed README file.
- Issue template.
- Code of conduct using Indonesian version of Contributor Covenant.
- Refer to wiki page for contribution guidelines.

### 2019-01-05 - v0.0.0

**Added**
- `hidrokit` as a module.
- Project documentation (readme, contributing, etc.).
- Usage notebook for `hidrokit`.

### 2018-10-20 - n/a

**Added**
- Created repository on GitHub.

---

[hidrokit]: https://hidrokit.github.io/hidrokit
[hidrokit-nb]: https://hidrokit.github.io/notebook
[hidrokit.readthedocs.io]: https://hidrokit.rtfd.io
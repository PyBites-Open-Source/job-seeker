# Change Log

## 0.0.4

- Removed Python 3.6 requirement
- Added automated TOX test for Python 3.7, 3.8, 3.9, 3.10 and 3.11
- Added Tox runner in GitHub Actions
- Added README badges
- Removed Jupyter Notebooks examples

### Added

- Example Jupyter Notebook `Jobs_Detailed.ipynb` analysis in `/example/notebooks`

## 0.0.3

### Changed

- included workType in the jobs_df
- cleaned up some unused variables from conftest.py

## 0.0.2

### Added

- MANIFEST.in
- Change log

### Changed

- included version in \_\_init\_\_\.py
- changed downloader module to download all job detail json response into a list of all jobs of the search
- changed test back to Mock class

### Removed

- VCR tests as they were unstable and unpredictable

## 0.0.1

Released on October 4, 2021.

### Added

- First version of the Python containing:
  - Tests,
  - Code style checking
  - License
  - README
  - Requirements.txt
  - Setup configuration

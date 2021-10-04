# Job Seeker

job_seeker is an utility to download data of a job search from seek.com.au into a csv file for data analysis and exploration

## Install using pip

```bash
pip install job-seeker
```

## Setting up to install from source

### download the package

```bash
git clone https://github.com/pedrojunqueira/job-seeker.git
```

### go to directory job-seeker on root path

```bash
cd job-seeker
```

## install from source

make sure you are on the root directory i.e. the directory where the setup.py file is located

then to install just do a `pip install .`

```bash
.
├── LICENSE
├── README.md
├── example
│   ├── job_seeker_usage.py
│   └── my_job_search.csv
├── job_seeker
│   ├── __init__.py
│   └── downloader.py
├── pyproject.toml
├── setup.py
└── tests
    ├── conftest.py
    ├── data
    │   └── response.json
    └── test_downloader.py
```

## Code example usage

```python

from job_seeker.downloader import JobSeeker

# set parameters

parameters = {
    "where" : "All Adelaide SA",
    "keywords" : "data analyst",
}

#instantiate the JobSeeker class

js = JobSeeker(params=parameters)

df = js.jobs_df

# df is a pandas.DataFrame object

# to print DataFrame head
print(df.head())


# to save as a csv in the current directory. See example on the ./example folder
df.to_csv("my_job_search.csv")

```

#### terminal output

```cmd
   page    job_id                         title  ...                       companyName                       company_advertiser
0     1  54150559                  Data Analyst  ...        Relationships Australia SA  Relationships Australia South Australia
1     1  54111544              Business Analyst  ...                    Robert Walters                           Robert Walters
2     1  54153618                  Data Analyst  ...                 Stoller Australia                        Stoller Australia
3     1  54150559                  Data Analyst  ...        Relationships Australia SA  Relationships Australia South Australia
4     1  54120381  Performance Insights Analyst  ...  Australian Institute of Business         Australian Institute of Business
```

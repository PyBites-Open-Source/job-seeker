from job_seeker.downloader import JobSeeker

# set parameters

parameters = {
    "where": "All Adelaide SA",
    "keywords": "data analyst",
}

# instantiate class

js = JobSeeker(params=parameters)

df = js.jobs_df

# df is a pandas.DataFrame object

# to print DataFrame head
print(df.head())

# to save as a csv
df.to_csv("my_job_search.csv")

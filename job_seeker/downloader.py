from collections import defaultdict

import pandas as pd
import requests


class JobSeeker:

    SEEK_API_URL = "https://www.seek.com.au/api/chalice-search/search"
    SEEK_API_URL_JOB = "https://chalice-experience-api.cloud.seek.com.au/job"

    def __init__(self, params: dict) -> None:

        self.default_params = dict(
            siteKey="AU-Main",
            sourcesystem="houston",
            page="1",
            seekSelectAllPages="true",
        )
        self.params = dict(self.default_params, **params)
        self.total_count = self._get_jobs_count()
        self.jobs_df = self._current_jobs_to_df()
        self.df_io = self._df_to_io_output(self.jobs_df)
        self.jobs_id = self._extract_list_job_ids()
        self.jobs_detail_json = None

    def _get_jobs_count(self) -> int:
        r = requests.get(url=self.SEEK_API_URL, params=self.params)
        json_response = r.json()
        return json_response.get("totalCount")

    def _total_pages(self, jobs_count) -> int:
        return int(round(jobs_count / 20, 0))

    def _current_jobs_to_df(self) -> pd.DataFrame:

        jobs_data = defaultdict(list)

        for page in range(1, self._total_pages(self.total_count) + 1):

            q_params = self.params
            q_params["page"] = str(page)

            r = requests.get(self.SEEK_API_URL, params=q_params)
            if r.ok:

                data = r.json()

                for job in data.get("data"):
                    job_id = job.get("id")
                    listing_date = job.get("listingDate")
                    title = job.get("title")
                    teaser = job.get("teaser")
                    company_advertiser = job.get("advertiser")["description"]
                    classification = job.get("classification")["description"]
                    location = job.get("location")
                    salary = job.get("salary")
                    companyName = job.get("companyName")
                    role_id = job.get("roleId")
                    isPrivateAdvertiser = job.get("isPrivateAdvertiser")
                    suburbWhereValue = job.get("suburbWhereValue")
                    subClassification = job.get("subClassification")["description"]
                    workType = job.get("workType")

                    jobs_data["page"].append(page)
                    jobs_data["job_id"].append(job_id)
                    jobs_data["title"].append(title)
                    jobs_data["role_id"].append(role_id)
                    jobs_data["listing_date"].append(listing_date)
                    jobs_data["teaser"].append(teaser)
                    jobs_data["classification"].append(classification)
                    jobs_data["subClassification"].append(subClassification)
                    jobs_data["location"].append(location)
                    jobs_data["suburbWhereValue"].append(suburbWhereValue)
                    jobs_data["salary"].append(salary)
                    jobs_data["companyName"].append(companyName)
                    jobs_data["company_advertiser"].append(company_advertiser)
                    jobs_data["isPrivateAdvertiser"].append(isPrivateAdvertiser)

        jobs_df = pd.DataFrame(jobs_data)

        return jobs_df

    def _df_to_io_output(self, df):
        return df.to_csv(index=False)

    def _extract_list_job_ids(self)-> list:
        if "job_id" in self.jobs_df.columns:
            return self.jobs_df["job_id"].to_list()

    def get_jobs_detail_json(self):
        jobs_detail = list()
        for job in self.jobs_id:
            r = requests.get(f"{self.SEEK_API_URL_JOB}/{job}")
            if r.ok:
                job_data = r.json()
                jobs_detail.append(job_data)
        return jobs_detail


from unittest.mock import patch
import json
from pathlib import Path

import pytest

from job_seeker.downloader import JobSeeker

parent = (Path(__file__).absolute().parent)

parameters = {
    "where" : "All Adelaide SA",
    "keywords" : "data analyst",
}

def mocked_requests_get(url: str, params: dict = None):
    if params:
        default_params = dict(
            siteKey="AU-Main",
            sourcesystem="houston",
            page="1",
            seekSelectAllPages="true",
            )
        params = dict(params, **default_params)
        url += "?"
        for k, v in params.items():
            url += f"{k}={v}&"

    url = url.strip("&")
    url = "+".join(url.split(" "))

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.ok = True if status_code == 200 else False

        def json(self):
            return self.json_data

    if "https://www.seek.com.au/api/chalice-search/search" in url:
        with open( parent / "data/new_response.json", "r+") as fp:
            db = json.load(fp)
            page = params["page"]
            resp = db[int(page)-1]["content"]
            
        return MockResponse(resp, 200)
    
    if "https://chalice-experience-api.cloud.seek.com.au/job" in url:
        with open( parent / "data/response_detail_short.json", "r+") as fp:
            db = json.load(fp)
            job_id = url.split("/")[-1]
            resp = db[job_id]
        return MockResponse(resp, 200)

    return MockResponse(None, 404)

@pytest.fixture(scope="function")
def js_instance():
    with patch("requests.get", side_effect=mocked_requests_get):
        js = JobSeeker(params=parameters)
        yield js 

from unittest.mock import patch
import json
from pathlib import Path

import pytest

from job_seeker.downloader import JobSeeker
import requests

parent = (Path(__file__).absolute().parent)

parameters = {
    "siteKey": "AU-Main",
    "sourcesystem" : "houston",
    "where" : "All Adelaide SA",
    "page" : "1",
    "seekSelectAllPages" : "true",
    "keywords" : "data analyst",
}

def mocked_requests_get(url: str, params: dict = None):
    request_url = url
    if params:
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
        with open( parent / "data/response.json", "r+") as fp:
            resp = json.load(fp)
            resp["page"] = parameters["page"]
            
        return MockResponse(resp, 200)

    return MockResponse(None, 404)

@pytest.fixture(scope="function")
def js_instance():
    with patch("requests.get", side_effect=mocked_requests_get):
        js = JobSeeker(params=parameters)
        yield js
import os

import pytest

from job_seeker.downloader import JobSeeker


@pytest.fixture(scope="module")
def vcr_cassette_dir(request):
    return ""


@pytest.fixture(scope="module")
def js_instance(vcr):
    params = {
        "where": "All Adelaide SA",
        "keywords": "data analyst",
    }
    with vcr.use_cassette("tests/cassettes/jobseeker.yaml"):
        return JobSeeker(params=params)

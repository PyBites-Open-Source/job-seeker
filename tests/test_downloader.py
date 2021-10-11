import pandas as pd


def test_params_dic(js_instance):
    assert isinstance(js_instance.params, dict)


def test_total_count(js_instance):
    assert js_instance.total_count == 40


def test_get_total_count(js_instance):
    total_count = js_instance._get_jobs_count()
    assert total_count == 40


def test_get_pages(js_instance):
    total_count = js_instance._get_jobs_count()
    pages = js_instance._total_pages(total_count)
    assert pages == 2


def test_df_instance(js_instance):
    df = js_instance.jobs_df
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (40, 15)
    assert df["page"].max() == 2


def test_df_io_output(js_instance):
    io_output = js_instance.df_io
    assert isinstance(io_output, str)

def test_job_ids(js_instance):
    job_ids = js_instance._extract_list_job_ids()
    assert isinstance(job_ids, list)

def test_get_job_details(js_instance):
    job_details = js_instance.get_jobs_detail_json()
    assert isinstance(job_details, list)
    assert isinstance(job_details[0], dict)
    assert len(job_details) == 40

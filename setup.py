from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="job_seeker",
    version="0.0.4",
    author="Pedro Junqueira",
    author_email="pedrocj@gmail.com",
    description="An utility downloader for a job search at seek.com.au",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PyBites-Open-Source/job-seeker",
    project_urls={
        "Bug Tracker": "https://github.com/PyBites-Open-Source/job-seeker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=["pandas", "requests"],
    python_requires=">=3.7, <=3.11",
)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="job_seeker",
    version="0.0.1",
    author="Pedro Junqueira",
    author_email="pedrocj@gmail.com",
    description="An utility downloader for job searcher at seek.com.au",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pedrojunqueira/job-seeker",
    project_urls={
        "Bug Tracker": "https://github.com/pedrojunqueira/job-seeker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=["pandas", "requests"],
    python_requires=">=3.6",
)

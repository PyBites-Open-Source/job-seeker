from setuptools import setup, find_packages
setup(
    name = 'job_seeker',
    packages = find_packages(),
)


# from setuptools import setup
# from setuptools import find_namespace_packages

# # Open the README file.
# with open(file="README.md", mode="r") as fh:
#     long_description = fh.read()

# setup(

#     name='job_seeker',

#     # Define Author Info.
#     author='Pedro Junqueira',
#     author_email='pedrocj@gmail.com',

#     # Define Version Info.
#     version='0.0.1',

#     # Define descriptions.
#     description='Utility tool to download data from seek.com.au',
#     long_description=long_description,
#     long_description_content_type="text/markdown",

#     # Define repo location.
#     url='https://github.com/pedrojunqueira/job-seeker.git',

#     # Define dependencies.
#     install_requires=[
#         'pandas',
#         'requests'
#     ],

#     # Specify folder content.
#     packages=find_namespace_packages(
#         include=['job_seeker']
#     ),

#     # Define the python version.
#     python_requires='>3.7',

#     # Define our classifiers.
#     classifiers=[

#         # License that guides my library.
#         'License :: OSI Approved :: MIT License',

#         # Package was written in English.
#         'Natural Language :: English',

#         # Operating systems.
#         'Operating System :: OS Independent',

#         # Programming Languages Used..
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3.8',

#         # Topics.
#         'Topic :: JobSearch',
#     ]

# )


import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file (from PYPI.md)
README = (HERE / "PYPI.md").read_text()

# This call to setup() does all the work
setup(
    name="un-treaties",
    version="0.1.2",
    description="Push countries to ratify UN treaties",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DataForGood-Norway/un_treaties",
    author="Data For Good - Norway",
    author_email="contact@dataforgood.no",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "beautifulsoup4", "connexion", "html5lib", "lxml", "pandas", "pycountry", "requests"
    ],
    entry_points={
        "console_scripts": [
            "un_crawl=un_treaties.crawler.get_data:main",
            "un_serve=un_treaties.rest_api.api:main",
        ]
    },
)

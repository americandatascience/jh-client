# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "jh-client"
VERSION = "1.1.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="JupyterHub REST API",
    author="Andrew Chang",
    url="https://amdatascience.com",
    keywords=["OpenAPI", "OpenAPI-Generator", "JupyterHub"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="BSD-3-Clause",
    long_description_content_type='text/markdown',
    long_description="""\
    The REST API for JupyterHub
    """,  # noqa: E501
    package_data={"openapi_client": ["py.typed"]},
)

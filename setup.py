#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README') as readme_file:
    readme = readme_file.read()

from pip.req import parse_requirements
requirements = [str(i.req) for i in parse_requirements("requirements.txt", session=False)]
test_requirements = [str(i.req) for i in parse_requirements("test_requirements.txt", session=False)]

VERSION = '0.1'

setup(
    name='theharvester',
    version=str(VERSION),
    description='theharvester in a library',
    long_description=readme,
    author='esiea security club',
    author_email='damdam.gold@gmail.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='theHarvester',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points="""
    [console_scripts]
    theharvester=theharvester.theHarvester:start
    """
)

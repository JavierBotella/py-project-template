#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme + '\n\n' + history,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    packages=find_packages('src'),
    package_dir={'': 'src/'},
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug.replace('_','-') }}={{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}:cli',
            'program_name2={{ cookiecutter.project_slug }}.py_proram2:func',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    test_suite='tests'
)

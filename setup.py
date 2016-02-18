# -*- coding: UTF-8 -*-

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-giom',
    version='0.1.build_number',
    packages=['giom_data'],
    include_package_data=True,
    license='MIT License',
    description='django GIOM meteo station data reader celery based measure tool',
    long_description=README,
    url='https://webeye.services/',
    author='Václav Rak',
    author_email='rak@webeye.services',
    classifiers=[
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Logging',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7'
    ],
)



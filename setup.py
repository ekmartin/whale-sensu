#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Whale Monitoring'
__email__ = 'contact@whale.io'
__version__ = '0.0.1'
__description__ = 'whale-sensu handles Sensu messages and redirects them into the ' \
                  'Whale Monitoring Platform.'
__url__ = 'https://github.com/WhaleMonitoring/whale-sensu'
__year__ = '2015'

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


requirements = [
    'whale-api',
    'six',
    'requests'
]
test_requirements = [
    'pytest',
    'mock',
    'coverage'
]

setup(
    name='whale-sensu',
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__email__,
    url=__url__,
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='whale-sensu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        "console_scripts": ['whale-sensu-handler = whale_sensu.handler:run_handler']
    },
    test_suite='tests',
    tests_require=test_requirements
)

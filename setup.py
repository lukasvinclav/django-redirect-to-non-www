#!/usr/bin/env python
from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    name='django-redirect-to-non-www',
    short_description='Redirect www URL addresses to non-www',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.0',
    packages=[
        'redirect_to_non_www',
    ],
    include_package_data=True,
    install_requires=('django', ),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
    ],
    keywords="django redirect www non-www"
)

#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='method_working_remotely',
    version='0.1.2',
    description='Yet Another RPC Framework.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='MWR Organization',
    author_email='mwr@mwr.wiki',
    url='https://github.com/mwr-wiki/method-working-remotely',
    py_modules=['method_working_remotely'],
    scripts=['method_working_remotely.py'],
    license='MIT',
    platforms='any',
    classifiers=['Operating System :: OS Independent',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
                 'Topic :: Software Development :: Libraries :: Application Frameworks',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 ],
)

#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='mbox-uploader-osx-tb',
      version='1.0',
      description='Thunderbird|GMail mbox uploader for OS X',
      author='Doug Campbell',
      author_email='wdouglascampbell@hotmail.com',
      url='https://github.com/wdouglascampbell/mbox-uploader-osx-tb',
      packages=find_packages(),
      license='GPLv3',
      install_requires=[
          'google-api-python-client',
      ],
     )

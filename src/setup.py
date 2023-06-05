#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name   ='OppFiller',
    version='0.1.0',
    author='Fernando Pujaico Rivera',
    author_email='fernando.pujaico.rivera@gmail.com',
    packages=['OppFiller'],
    #scripts=['bin/script1','bin/script2'],
    url='https://github.com/trucomanx/oppfiller',
    license='GPLv3',
    description='filler of OpenPifPaf data',
    #long_description=open('README.txt').read(),
    install_requires=[
       "numpy" #"Django >= 1.1.1",
    ],
)

#! python setup.py sdist bdist_wheel
# Upload to PyPi
# or 
#! pip3 install dist/OppFiller-0.1.0.tar.gz 

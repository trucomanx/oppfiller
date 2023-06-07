#!/usr/bin/python

from setuptools import setup, find_packages
import os 

def func_read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read();

setup(
    name   ='OppFiller',
    version='0.1.0',
    author='Fernando Pujaico Rivera',
    author_email='fernando.pujaico.rivera@gmail.com',
    maintainer='Fernando Pujaico Rivera',
    maintainer_email='fernando.pujaico.rivera@gmail.com',
    #scripts=['bin/script1','bin/script2'],
    url='https://github.com/trucomanx/oppfiller',
    license='GPLv3',
    description='Filler of OpenPifPaf data',
    #long_description=func_read('README.txt'),
    include_package_data=True,
    packages=['OppFiller'],
    package_dir={'OppFiller':'OppFiller'},
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        #'': ['*.py','*.h5'],
        'OppFiller': ['*.py','models/model_sequence1/*.h5','models/model_sequence2/*.h5']
    },
    install_requires=[
       "openpifpaf",
       "tensorflow",
       "matplotlib",
       "numpy" #"Django >= 1.1.1",
    ],
)

#! python setup.py sdist bdist_wheel
# Upload to PyPi
# or 
#! pip3 install dist/OppFiller-0.1.0.tar.gz 

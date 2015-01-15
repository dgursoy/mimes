#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import warnings

from setuptools import setup, Extension, find_packages

# Set Python package requirements for installation.
install_requires = ['numpy>=1.8.0', 'scipy>=0.13.2', 'h5py>=2.2.1']

# Enforce these same requirements at packaging time
import pkg_resources

for requirement in install_requires:
    try:
        pkg_resources.require(requirement)
    except pkg_resources.DistributionNotFound:
        msg = 'Python package requirement not satisfied: ' + requirement
        msg += '\n\nInstall all required packages with\n\tpip install -r requirements.txt'
        raise pkg_resources.DistributionNotFound, msg

# Main setup configuration.
setup(
    name='mimes',
    version=open('VERSION').read().strip(),
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    author='Doga Gursoy, Cd Phatak',
    description='MIMES: Multimodal Imaging of Materials for Energy Storage',
    keywords=['registration', 'phase retrieval', 'tomography', 'reconstruction', 'imaging'],
    download_url='http://github.com/dgursoy/mimes',
    license='BSD',
    platforms='Any',
    classifiers=['Development Status :: 5 - Beta',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Science/Research',
                 'Intended Audience :: Education',
                 'Intended Audience :: Developers',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: C',
                 'Programming Language :: C++'])

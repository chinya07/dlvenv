from setuptools import setup, find_packages
import codecs
import os

with open("README.md") as f:
    long_description = f.read()

VERSION = '0.0.1'
DESCRIPTION = 'dlvenv helps you to setup an environment for Deep Learning in a single line of code with all dependencies'

# Setting up
setup(
    name="dlvenv",
    version=VERSION,
    author="chinya07",
    author_email="kaundanyachinmaya07@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'scipy',
                      'scikit-learn', 'pyforest', 'pycaret', 'Theano',
                      'tensorflow-cpu'],
    keywords=['dlvenv', 'Deep Learning environment installation in single line', 'data science', 'deep learning', 'deep learning environment'],
    url='http://github.com/ashishpatel26/datascienv',
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    platforms=["any"],
    zip_safe=True,
)

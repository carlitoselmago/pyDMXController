from setuptools import setup, find_packages
from pyDMXController.pyDMXController import __version__

setup(
    name='pyDMXController',
    version=__version__,
    packages=find_packages(),
    install_requires=[
       "pyserial"
    ],
    url='https://github.com/carlitoselmago/pyDMXController',
    author='Carlos Carbonell',
    author_email='ccarbonell@gmail.com',
    description='A simple Python package for DMX controller'
)
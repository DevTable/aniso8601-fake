import sys

try:
    from setuptools import setup
except ImportError:
    from distutils import setup

readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()

setup(
    name='aniso8601',
    version='1.00',
    description='A fake replacement library for the aniso8601 library.',
    long_description=README_TEXT,
    author='Jake Moshenko',
    author_email='jake@devtable.com',
    url='https://github.com/DevTable/aniso8601-fake',
    packages=['aniso8601'],
    package_dir={
        'aniso8601' : 'aniso8601',
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

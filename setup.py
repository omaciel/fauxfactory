"""A setuptools-based script for installing FauxFactory."""
# setuptools is preferred over distutils.
import codecs
import os

from setuptools import find_packages, setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    filename = os.path.join(*paths)
    with codecs.open(filename, mode='r', encoding='utf-8') as handle:
        return handle.read()


LONG_DESCRIPTION = (read('README.rst') + '\n\n' +
                    read('AUTHORS.rst') + '\n\n' +
                    read('HISTORY.rst'))

setup(
    name='fauxfactory',
    description='Generates random data for your tests.',
    long_description=LONG_DESCRIPTION,
    use_scm_version=True,
    author='Og Maciel',
    author_email='omaciel@ogmaciel.com',
    url='https://github.com/omaciel/fauxfactory',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    keywords='python automation data',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Testing',
    ],
    test_suite='tests',
)

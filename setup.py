import os

from distutils.core import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

long_description = (read('README.rst') + '\n\n' +
                    read('AUTHORS.rst') + '\n\n' +
                    read('HISTORY.rst'))

setup(
    name='fauxfactory',
    description='Generates random data for your tests.',
    long_description=long_description,
    version='2.0.3',
    author='Og Maciel',
    author_email='omaciel@ogmaciel.com',
    url='https://github.com/omaciel/fauxfactory',
    packages=['fauxfactory'],
    keywords='python automation data',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing',
    ]
)

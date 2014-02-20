from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='fauxfactory',
    version='0.1.0',
    url='https://github.com/omaciel/fauxfactory',
    author='Og Maciel',
    author_email='omaciel@redhat.com',
    packages=['fauxfactory'],
    long_description=long_description,
)

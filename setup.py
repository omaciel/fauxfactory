from distutils.core import setup

with open('LICENSE') as file:
    license = file.read()

with open('README.md') as file:
    long_description = file.read()

setup(
    name='fauxfactory',
    version='0.1.0',
    url='https://github.com/omaciel/fauxfactory',
    author='Og Maciel',
    author_email='omaciel@redhat.com',
    packages=['fauxfactory'],
    description='Generates random data for your tests.',
    long_description=long_description,
    license=license,
)

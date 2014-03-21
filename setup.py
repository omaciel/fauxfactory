from distutils.core import setup

with open('LICENSE') as file:
    license = file.read()

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='fauxfactory',
    description='Generates random data for your tests.',
    long_description=long_description,
    version='0.1.2',
    author='Og Maciel',
    author_email='omaciel@redhat.com',
    url='https://github.com/omaciel/fauxfactory',
    packages=['fauxfactory'],
    license=license,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ]
)

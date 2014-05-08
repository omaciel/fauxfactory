from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()
with open('AUTHORS.rst') as f:
    authors = f.read()

long_description = readme + '\n\n' + authors + '\n\n' + history

setup(
    name='fauxfactory',
    description='Generates random data for your tests.',
    long_description=long_description,
    version='0.2.0',
    author='Og Maciel',
    author_email='omaciel@redhat.com',
    url='https://github.com/omaciel/fauxfactory',
    packages=['fauxfactory'],
    keywords='python automation data',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
    ]
)

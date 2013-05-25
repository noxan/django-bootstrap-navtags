import os
from setuptools import setup, find_packages

import bootstrapnavtags


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-bootstrap-navtags',
    version=bootstrapnavtags.__version__,
    description='Navigation templatetags for django with twitter bootstrap.',
    long_description=read('README.md'),
    license='MIT License',
    author='Richard Stromer',
    author_email='noxan@byteweaver.org',
    url='https://github.com/noxan/django-bootstrap-navtags',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
    ],
    test_suite='bootstrapnavtags.tests',
)

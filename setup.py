import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'pyconfig', '__init__.py')
version_line = [line for line in open(module_path) if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="PyConfig",
    version=__version__,
    url="https://github.com/cngo-github/pyconfig",

    author="Chuong Ngo",
    author_email="cngo-github@gmail.com",

    description="An easy-to-use package for storing and accessing global configuration values.",
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(),

    zip_safe=False,
    platforms='any',

    classifiers=[
        'Development Status :: 3 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

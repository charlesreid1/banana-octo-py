"""
BANANA OCTO PY
A simple Python package

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

long_description = 'this is a simple Python project, and this is a long description'

setup(
    name='banana_octo_py',
    version='1.0',

    description='a simple Python project',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/charlesreid1/banana-octo-py',

    # Author details
    author='charles reid',
    author_email='not_one_email@notevenonce.com',

    # Choose your license
    license='MIT',

    ## You can just specify the packages manually here if your project is
    ## simple. Or you can use find_packages().
    #packages=(['banana_octo_py']),
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],
    #
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy'],

    ## List additional groups of dependencies here (e.g. development
    ## dependencies). You can install these using the following syntax,
    ## for example:
    ## $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'sample': ['banana_octo_py/package_data.dat'],
    },

    ### # Although 'package_data' is the preferred approach, in some case you may
    ### # need to place data files outside of your packages. See:
    ### # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    ### # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    ### data_files=[('my_data', ['data/data_file'])],

    ### # To provide executable scripts, use entry points in preference to the
    ### # "scripts" keyword. Entry points provide cross-platform support and allow
    ### # pip to create the appropriate form of executable for the target platform.
    ### entry_points={
    ###     'console_scripts': [
    ###         'sample=sample:main',
    ###     ],
    ### },
)

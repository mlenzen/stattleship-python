#!/usr/bin/env python
from codecs import open
import os
from setuptools import setup


# Get the long description from the relevant file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
	long_description = f.read()

requirements = [
	'setuptools',
	'requests',
	]

setup(
	name='stattlepy',
	version='0.0.1',
	description='',
	long_description=long_description,
	keywords='stattleship sports statistics',
	author='Michael Lenzen',
	author_email='m.lenzen@gmail.com',
	license='MIT',
	url='https://github.com/mlenzen/stattleship-python',
	py_modules=['stattlepy'],
	include_package_data=True,
	zip_safe=False,
	package_data={
		'': ['README.md', 'LICENSE'],
		},
	install_requires=requirements,
	# See: http://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development',
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: Implementation :: PyPy',
		],
	)

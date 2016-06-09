README
######

This package includes one module ``stattlepy`` for accessing the Stattleship
API.

:Stattleship Homepage: https://www.stattleship.com/
:API Docs: http://developers.stattleship.com/

Installation
============

``pip install git+https://github.com/mlenzen/stattleship-python.git``

Usage
=====
.. code:: python

	>>> import stattlepy
	>>> stattle = stattlepy.Stattleship('your_token')
	>>> stattle.get('hockey', 'nhl', 'teams')
	...

Instead of passing the token to Stattleship __init__ you can set an environment
variable.

.. code:: sh

	$ export STATTLESHIP_TOKEN='your_token'
	$ python

.. code:: python

	>>> import stattlepy
	>>> stattle = stattlepy.Stattleship()
	>>> ...

Logging is done through the logging module, so if you want to see messages:

.. code:: python

	>>> import logging
	>>> logging.basicConfig()
	>>> ...

:Author: Michael Lenzen
:Copyright: 2016 Michael Lenzen
:License: MIT
:GitHub: https://github.com/mlenzen/stattleship-python

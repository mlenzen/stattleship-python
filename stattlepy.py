"""stattlepy - Implement Stattleship API.

Install:
	pip install git+https://github.com/mlenzen/stattleship-python.git

Usage:
	import stattlepy
	stattle = stattlepy.Stattleship('your_token')
	stattle.get('hockey', 'nhl', 'teams')

Alternatively, your access token can be set using an environment variable.

Stattleship: https://www.stattleship.com/
API Docs: http://developers.stattleship.com/
"""
from __future__ import absolute_import, unicode_literals
import logging
import os
import time

import requests

__version__ = '0.0.1'
__repo_url__ = 'https://github.com/mlenzen/stattleship-python'

USER_AGENT = 'stattlepy/{version} {url}'.format(
	version=__version__,
	url=__repo_url__,
	)
ENV_TOKEN_VAR_NAME = 'STATTLESHIP_TOKEN'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class Stattleship():
	"""Stattleship API access object."""

	def __init__(self, token=None):
		"""Create a Stattleship API access object.

		Access token must either be passed or available in the os environment.

		Args:
			token (str): Stattleship Access Token
		"""
		token = token or os.environ.get(ENV_TOKEN_VAR_NAME)
		if not token:
			raise ValueError(
				'Must pass token or set environment variable %s' % ENV_TOKEN_VAR_NAME
				)
		self.session = requests.Session()
		self.session.headers.update({
			'Authorization': token,
			'Content-Type': 'application/json',
			'User-Agent': USER_AGENT,
			})

	def get_v1(self, sport, league, ep, walk=False, stat_type=None, **params):
		"""Implement version 1 of the API."""
		url_format = 'https://www.stattleship.com/{sport}/{league}/{ep}'
		version = 1
		sport = sport.lower()
		league = league.lower()
		ep = ep.lower()
		if params.get('page') == 1:
			del params['page']
		if stat_type:
			params['type'] = stat_type
		logger.info('Making initial request')
		url = url_format.format(
			sport=sport,
			league=league,
			ep=ep,
			)
		response = self._get(version, url, params=params)
		data = response.json()
		if walk:
			while response.links['next']:
				time.sleep(0.1)
				logger.info('Getting additional request')
				next_link = response.links['next']['url']
				response = self._get(version, next_link)
				data.append(response.json())
		logger.info('All requests complete')
		return data

	get = get_v1

	def _get(self, api_version, url, params=None):
		headers = {
			'Accept': 'application/vnd.stattleship.com; version=%s' % api_version,
			}
		response = self.session.get(url, params=params, headers=headers)
		response.raise_for_status()
		return response

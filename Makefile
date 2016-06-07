.PHONY: help tests testall clean lint coverage publish

help:
	@echo "  clean       remove unwanted files like .pyc's"
	@echo "  lint        check style with flake8"
	@echo "  tests       run tests (using py.test)"
	@echo "  testall     run tests for all Python versions (using tox)"
	@echo "  coverage    run coverage report"
	@echo "  publish     publish to PyPI"
	@echo "  docs        create HMTL docs (using Sphinx)"

tests:
	python setup.py test

testall:
	tox

clean:
	rm -rf build
	rm -rf dist
	rm -rf stattlepy.egg-info
	find . -name *.pyc -delete
	find . -name *.pyo -delete
	find . -name *~ -delete
	find . -name __pycache__ -delete

lint:
	flake8 --statistics --count

coverage:
	coverage run --source stattlepy setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

publish: testall lint
	python setup.py sdist upload
	python setup.py bdist_wheel upload

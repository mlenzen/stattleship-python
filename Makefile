.PHONY: help clean lint publish

help:
	@echo "  clean       remove unwanted files like .pyc's"
	@echo "  lint        check style with flake8"
	@echo "  publish     publish to PyPI"
	@echo "  docs        create HMTL docs (using Sphinx)"

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

publish: lint
	python setup.py sdist upload
	python setup.py bdist_wheel upload

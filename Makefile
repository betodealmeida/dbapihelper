init: requirements
	pip install -r requirements.txt

test:
	nosetests tests

requirements:
	pipreqs --force dbapihelper --savepath requirements.txt

.PHONY: init test requirements

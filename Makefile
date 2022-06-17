intall:
	pip install -e .["dev"]

test:
	FLASK_ENV=test pytest tests/ -v 
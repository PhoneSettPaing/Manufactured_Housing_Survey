install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py
	
lint:
	pylint --disable=R,C getdata.py
	

test:
	python -m pytest -vv --cov=getdata test_getdata.py
	
run:
	python3 getdata.py
	
all: install format lint test run
.PHONY: install
install:
	pip3 install -r requirements.txt

.PHONY: run
run:
	python3 app/main.py

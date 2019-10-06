.PHONY: install
install:
	pip3 install -r requirements.txt

.PHONY: run
run:
	python3 app/main.py

.PHONY: start
start:
	supervisord

.PHONY: stop
stop:
	killall supervisord
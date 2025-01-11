NAME=probaility-playmakers
WORKDIR = $(shell pwd)
PYTHONPATH:= $(PYTHONPATH):$(WORKDIR)
DOT_ENV = $(WORKDIR)/.env

run:
	export PYTHONPATH=$(PYTHONPATH)
	streamlit run app/main.py


include Makefile.venv
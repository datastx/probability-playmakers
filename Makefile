NAME=probability-playmakers
WORKDIR = $(shell pwd)
PYTHONPATH := $(PYTHONPATH):$(WORKDIR)
DOT_ENV = $(WORKDIR)/.env

SHELL := /bin/bash

run:
	# All commands run in one shell invocation by separating them with semicolons or backslashes
	export PYTHONPATH=$(PYTHONPATH); \
	set -o allexport; source $(DOT_ENV); set +o allexport; \
	.venv/bin/streamlit run app/create_users.py

include Makefile.venv

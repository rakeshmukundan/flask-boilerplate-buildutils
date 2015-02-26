VENV_LOCATION=.venv
VENV_ACTIVATE="$(VENV_LOCATION)/bin/activate"

debug: venv
	. .env; python run.py $(ARGS) --debug


venv: $(VENV_LOCATION)

$(VENV_LOCATION): Application/requirements.txt
	. .env;
	touch $(VENV_LOCATION)


uninstall:
	rm -rf $(VENV_LOCATION)
VENV_LOCATION=.venv
VENV_ACTIVATE="$(VENV_LOCATION)/bin/activate"

debug: venv
	. .env && python run.py server $(ARGS) --debug

venv: $(VENV_LOCATION)

$(VENV_LOCATION): Application/requirements*.txt
	. .env && pip3 install -r Application/requirements.txt --upgrade
	touch $(VENV_LOCATION);
	$(eval CONFIG_CLASS := $(shell . .env && python3 -m config))
	test -e 'Application/requirements-$(CONFIG_CLASS).txt' && pip3 install -r 'Application/requirements-$(CONFIG_CLASS).txt' --upgrade


clean:
	rm -rf $(VENV_LOCATION)
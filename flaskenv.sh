#!/usr/bin/env bash

if type deactivate &> /dev/null; then
    deactivate;
fi

if [ -e .venv/bin/activate ]; then
    . .venv/bin/activate;
else
    virtualenv -p `which python3` .venv;
    . .venv/bin/activate;
    upgrade;
fi

upgrade() {
    pip3 install -r reqs/requirements.txt --upgrade;
    CONFIG_CLASS=`python3 -m config`
    test -e "reqs/requirements-${CONFIG_CLASS}.txt" && 
    pip3 install -r "reqs/requirements-${CONFIG_CLASS}.txt" --upgrade
}
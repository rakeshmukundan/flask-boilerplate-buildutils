#!/usr/bin/env bash

if type deactivate &> /dev/null; then
    deactivate;
fi

if [ -e .venv/bin/activate ]; then
    . .venv/bin/activate;
else
    virtualenv -p `which python3` .venv;
    . .venv/bin/activate;
    pip3 install -r Application/requirements.txt;
fi

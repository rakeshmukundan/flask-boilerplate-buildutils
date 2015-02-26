#!/usr/bin/env bash


if [ -e '.env' ]; then
    upgrade() {
        pip3 install -r reqs/requirements.txt --upgrade;
        CONFIG_CLASS=`python3.4 -m config`
        test -e "reqs/requirements-${CONFIG_CLASS}.txt" && 
        pip3 install -r "reqs/requirements-${CONFIG_CLASS}.txt" --upgrade
    }

    setup_db() {
        CONFIG_CLASS=`python3.4 -m config`
        DB_DATABASE=`python3.4 -m config -k DB_DATABASE`
        DB_USERNAME=`python3.4 -m config -k DB_USERNAME`

        case $CONFIG_CLASS in
            MySQLStd)  echo "CREATE DATABASE IF NOT EXISTS ${DB_DATABASE}" | mysql -u ${DB_USERNAME};;
            CI)  echo "CREATE DATABASE IF NOT EXISTS ${DB_DATABASE}" | mysql -u ${DB_USERNAME};;
        esac
    }

    # Override cd to detect when we escape 
    cd() {
        builtin cd "$@";
        if ! [[ `pwd` == $VENV_DIR* ]]; then
            # User just left the venv. Return them to their normal CD functionality.
            deactivate;
            unset -f setup_db;
            unset -f upgrade;
            
            cd() {
                builtin cd "$@"
                if type autoenv_init &> /dev/null; then
                    autoenv_init 
                fi
            }
        fi
    }


    if type deactivate &> /dev/null; then
        deactivate;
    fi

    if [ -e .venv/bin/activate ]; then
        . .venv/bin/activate;
    else
        virtualenv -p `which python3.4` .venv;
        . .venv/bin/activate;
        upgrade;
        setup_db;
    fi

    export VENV_DIR=`pwd`;

fi
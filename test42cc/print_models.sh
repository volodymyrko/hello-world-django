#!/bin/bash

DIR=`dirname $0`
DATE=`date "+%Y-%m-%d"`
LOG_FILE=${DIR}/${DATE}.dat

${DIR}/manage.py print_models 2>${LOG_FILE}

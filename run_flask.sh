#!/bin/bash

export FLASK_APP=hello.py
export FLASK_ENV=development

flask run --host=0.0.0.0

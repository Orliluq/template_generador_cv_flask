#!/bin/sh

source venv/Scripts/activate

export FLASK_APP=main 
export PORT=${PORT:-5000}

python -m flask run --debug -p $PORT
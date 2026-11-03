#!/bin/bash

cd /c/automation/git_python_repo

source venv/Scripts/activate

behave --tags=@Framework --format=pretty --junit --junit-directory=reports/junit --no-capture --no-capture-stderr

time(10000)

behave --tags=@Framework --format=pretty --junit --junit-directory=reports/junit --no-capture --no-capture-stderr
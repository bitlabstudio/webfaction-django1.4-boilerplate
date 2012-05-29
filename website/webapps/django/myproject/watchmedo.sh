#!/bin/bash
watchmedo shell-command --recursive --ignore-directories --patterns="*.py" --command='fab test' .

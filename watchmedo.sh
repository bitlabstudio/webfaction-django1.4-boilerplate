#!/bin/bash
watchmedo shell-command --ignore-directories --recursive --wait --pattern "*.py" --command='cd docs && fab html' website

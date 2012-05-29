#!/bin/bash
watchmedo shell-command --ignore-directories --recursive --wait --pattern "*.py" --wait --command='cd docs && fab html' website

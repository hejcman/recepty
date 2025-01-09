#!/bin/bash

# Check if we get the new project name.
if [ -z "$1" ]; then
    echo "No argument supplied"
    exit 1
fi

new_name=$1

# Update the source code directory name
mv "src/package" "src/${new_name}"

# Update the path in the apidoc target in docs/Makefile
sed -i "" "s|../src/package|..src/${new_name}|g" docs/Makefile

# Update the targets of .pre-commit-config.yml
sed -i "" "s|src/package|src/${new_name}|g" .pre-commit-config.yaml

# Update the targets in pyproject.toml
sed -i "" "s|src/package|src/${new_name}|g" pyproject.toml

# Update test imports
sed -i "" "s|src.package|src.${new_name}|g" tests/*.py

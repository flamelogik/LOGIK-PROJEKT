#!/bin/bash
# Recursively remove all files starting with ._ in the current directory and subdirectories

find . -type f -name '._*' -print -delete

echo "All ._ files have been removed."

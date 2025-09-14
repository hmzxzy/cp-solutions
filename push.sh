#!/bin/bash

# Ask for a problem name
read -p "Enter problem name: " PROBLEM_NAME

# Stage all files in current folder
git add .

# Commit with simple message
git commit -m "Solved $PROBLEM_NAME"

# Push to main branch
git push origin main

echo "Done"


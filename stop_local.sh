#!/bin/bash

# Find and kill the Ollama process
echo "Stopping Ollama..."
pkill ollama

# Deactivate the virtual environment if active
#if [[ "$VIRTUAL_ENV" != "" ]]; then
#    deactivate
#    echo "Virtual environment deactivated."
#fi

echo "Environment stopped."
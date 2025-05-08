#!/bin/bash

# Check if Ollama is already running
if ! curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "Starting Ollama..."
    ollama serve &
    
    # Wait for Ollama to start
    until curl -s http://localhost:11434/api/tags > /dev/null; do
        sleep 1
    done
fi

echo "Ollama is running!"

# Check if the model exists
if ! ollama list | grep -q "codellama:7b"; then
    echo "Pulling codellama:7b model (this may take a while)..."
    ollama pull codellama:7b
    echo "Model pulled successfully!"
fi

# Activate the virtual environment
source venv/bin/activate

# Ensure notebooks directory exists
mkdir -p notebooks

# Start Jupyter Notebook in the notebooks directory
jupyter notebook --notebook-dir=notebooks
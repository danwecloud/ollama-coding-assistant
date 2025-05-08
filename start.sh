#!/bin/bash

# Activate virtual environment
source /app/venv/bin/activate

# Start Ollama in the background
ollama serve &
OLLAMA_PID=$!

# Wait for Ollama to start
echo "Waiting for Ollama to start..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
    sleep 1
done
echo "Ollama is running!"

# Pull the model if it doesn't exist yet
if ! ollama list | grep -q "codellama:7b"; then
    echo "Pulling codellama:7b model (this may take a while)..."
    ollama pull codellama:7b
    echo "Model pulled successfully!"
fi

# Ensure notebooks directory exists
mkdir -p /app/notebooks

# Start Jupyter Notebook from the virtual environment
echo "Starting Jupyter Notebook..."
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password='' --notebook-dir=/app/notebooks

# If Jupyter exits, also kill Ollama
kill $OLLAMA_PID
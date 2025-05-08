# 🤖 Ollama Coding Assistant

A Python-based coding assistant that uses Ollama's codellama models to provide code completions, explanations, and refinements.

## Features

- Code completion based on prompts
- Code explanation
- Code refinement based on instructions
- Example Jupyter notebook integration

## Requirements

- Python 3.6+
- Ollama installed locally (for local usage)
- Docker and Docker Compose (for containerized usage)
- NVIDIA GPU with CUDA support (for optimal performance)

## Installation

### Local Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ollama-coding-assistant.git
   cd ollama-coding-assistant
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Install Ollama if you haven't already:
   ```
   curl -fsSL https://ollama.com/install.sh | sh
   ```

4. Pull the codellama model:
   ```
   ollama pull codellama:7b
   ```

## Usage

### Running Locally

1. Start the local environment:
   ```
   chmod +x start_local.sh
   ./start_local.sh
   ```

   This will:
   - Start the Ollama service
   - Activate the Python virtual environment
   - Launch Jupyter Notebook

2. To stop the local environment:
   ```
   chmod +x stop_local.sh
   ./stop_local.sh
   ```

### Running with Docker

1. Start the containerized environment:
   ```
   chmod +x start.sh
   ./start.sh
   ```

   Or use Docker Compose directly:
   ```
   docker-compose up -d
   ```

2. Access Jupyter Notebook at http://localhost:8888

3. To stop the Docker environment:
   ```
   docker-compose down
   ```

## Using the Code Assistant

```python
from ollama_coding_assistant import CodeAssistant

# Initialize the assistant
assistant = CodeAssistant(model="codellama:7b")

# Complete code
completion = assistant.complete("def fibonacci(n):\n    ")

# Explain code
explanation = assistant.explain_code("your code here")

# Refine code
refinement = assistant.refine_code(
    "original code",
    "instructions for refinement"
)
```

## Example Notebook

See `notebooks/example_notebook.ipynb` for usage examples.


## Helpful Commands

### List Ollama models already downloaded
   ```
      ollama list
   ```

### Check how much disk space Ollama models use
   ```
      du -sh ~/.ollama/models
   ```
### Remove a Model
   ```
      ollama rm stable-code:3b
   ```

### Get Model Details
   ``` 
      ollama show codellama:7b
   ```

## Project Structure

Current project structure after reorganization:

```
ollama-coding-assistant/
│
├── .github/workflows/           # GitHub Actions workflows
│   └── python-tests.yml         # Python testing workflow
│
├── docs/                        # Documentation files
│   └── usage.md                 # Detailed usage guide
│
├── notebooks/                   # Jupyter notebooks 
│   ├── README.md                # Notebooks documentation
│   └── example_notebook.ipynb   # Example usage notebook
│
├── ollama_coding_assistant/     # Python package directory
│   ├── __init__.py              # Package initialization
│   └── code_assistant.py        # Main code assistant class
│
├── tests/                       # Unit tests
│   ├── README.md                # Test documentation
│   ├── __init__.py              # Test package initialization
│   └── test_code_assistant.py   # Test cases
│
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT License
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup file
│
├── start_local.sh               # Script to start locally
├── stop_local.sh                # Script to stop local environment
├── start.sh                     # Script to start Docker environment
│
├── Dockerfile                   # Docker image definition
└── docker-compose.yml           # Docker Compose configuration
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.
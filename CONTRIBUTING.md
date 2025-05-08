# Contributing to Ollama Coding Assistant

Thank you for considering contributing to the Ollama Coding Assistant!

## Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## How to Contribute

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Run tests to ensure your changes don't break existing functionality
5. Commit your changes: `git commit -m 'Add some feature'`
6. Push to the branch: `git push origin feature/your-feature-name`
7. Submit a pull request

## Development Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
4. Install development dependencies: `pip install -r requirements-dev.txt` (if available) or `pip install -r requirements.txt`
5. Run tests: `pytest tests/`

## Testing

Run the tests with:

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=./ --cov-report=term-missing
```

## Pull Request Process

1. Update the README.md or documentation with details of changes if appropriate
2. Update the tests to cover your changes
3. The PR should work for Python 3.8 and above
4. Your PR will be merged once it passes all tests and is reviewed
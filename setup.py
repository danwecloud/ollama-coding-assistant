from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="ollama-coding-assistant",
    version="0.1.0",
    author="",
    author_email="",
    description="A Python-based coding assistant that uses Ollama's codellama models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ollama-coding-assistant",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    scripts=["start.sh", "start_local.sh", "stop_local.sh"],
    package_data={
        "": ["notebooks/*.ipynb", "docs/*.md"],
    },
)
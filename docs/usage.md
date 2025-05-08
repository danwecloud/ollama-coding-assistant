# Usage Guide

This document provides detailed usage instructions for the Ollama Coding Assistant.

## Basic Usage

### Initializing the Assistant

```python
from code_assistant import CodeAssistant

# Default initialization (uses codellama:7b on localhost)
assistant = CodeAssistant()

# Custom model and API endpoint
assistant = CodeAssistant(
    model="codellama:13b", 
    api_base="http://example-ollama-server:11434"
)
```

## Code Completion

Generate code completions based on a prompt:

```python
# Simple completion
completion = assistant.complete(
    "def calculate_fibonacci(n):\n    "
)

# With custom parameters
completion = assistant.complete(
    prompt="def sort_array(arr):\n    ",
    max_tokens=1000,
    temperature=0.2,
    stop=["# End"]
)
```

## Code Explanation

Get an explanation of existing code:

```python
explanation = assistant.explain_code("""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
""")
```

## Code Refinement

Refine code based on instructions:

```python
refinement = assistant.refine_code(
    """
    def search(arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
    """,
    "Refactor this to use binary search instead of linear search. Assume the array is sorted."
)
```

## Advanced Configuration

For advanced use cases, you can adjust various parameters to control the output:

- `max_tokens`: Control the length of the generated response
- `temperature`: Adjust the creativity level (0.0-1.0)
- `stop`: Provide custom stop sequences to end generation
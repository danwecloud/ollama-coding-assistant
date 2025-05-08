
import requests
from typing import Optional, Dict, Any, List

class CodeAssistant:
    """A simple client for Ollama-based coding assistance."""
    
    def __init__(self, model: str = "codellama:7b", api_base: str = "http://localhost:11434"):
        """Initialize the coding assistant.
        
        Args:
            model: The model to use for code generation
            api_base: The base URL for the Ollama API
        """
        self.model = model
        self.api_base = api_base.rstrip('/')
        self._check_connection()
    
    def _check_connection(self) -> None:
        """Check if the Ollama server is running and the model is available."""
        try:
            response = requests.get(f"{self.api_base}/api/tags")
            if response.status_code != 200:
                print(f"Warning: Ollama server returned status code {response.status_code}")
                return
            
            models = response.json().get("models", [])
            available_models = [m.get("name") for m in models]
            
            if self.model not in available_models:
                print(f"Warning: Model '{self.model}' not found in available models: {available_models}")
                print(f"You may need to run: ollama pull {self.model}")
            else:
                print(f"Connected to Ollama server with model: {self.model}")
        except requests.RequestException as e:
            print(f"Warning: Could not connect to Ollama server at {self.api_base}")
            print(f"Error: {str(e)}")
            print("Make sure Ollama is running with: ollama serve")
    
    def complete(self, 
                prompt: str, 
                max_tokens: int = 500,
                temperature: float = 0.5,
                stop: Optional[List[str]] = None) -> str:
        """Generate code completion based on a prompt.
        
        Args:
            prompt: The code prompt to complete
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature (0.0-1.0, lower is more deterministic)
            stop: List of strings to stop generation when encountered
            
        Returns:
            The generated code as a string
        """
        stop = stop or ["```"]
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens,
                "temperature": temperature,
                "stop": stop
            }
        }
        
        try:
            response = requests.post(f"{self.api_base}/api/generate", json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.RequestException as e:
            print(f"Error generating completion: {str(e)}")
            return ""
    
    def explain_code(self, code: str, max_tokens: int = 500) -> str:
        """Generate an explanation for the provided code.
        
        Args:
            code: The code to explain
            max_tokens: Maximum number of tokens to generate
            
        Returns:
            The explanation as a string
        """
        prompt = f"# Code to explain:\n```\n{code}\n```\n\n# Explanation of what this code does:\n"
        return self.complete(prompt, max_tokens=max_tokens, temperature=0.3)
    
    def refine_code(self, code: str, instructions: str, max_tokens: int = 500) -> str:
        """Refine code based on instructions.
        
        Args:
            code: The original code to refine
            instructions: Instructions describing how to refine the code
            max_tokens: Maximum number of tokens to generate
            
        Returns:
            The refined code as a string
        """
        prompt = f"# Original code:\n```\n{code}\n```\n\n# Instructions for refinement:\n{instructions}\n\n# Refined code:\n```\n"
        result = self.complete(prompt, max_tokens=max_tokens, temperature=0.5)
        
        # Clean up the result if needed
        if "```" in result:
            result = result.split("```")[0]
            
        return result

# Example usage
if __name__ == "__main__":
    print("This module should be imported. See notebooks for examples.")
    print("Try: from ollama_coding_assistant import CodeAssistant")
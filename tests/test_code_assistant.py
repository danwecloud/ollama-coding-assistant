import unittest
from unittest.mock import patch, MagicMock
from ollama_coding_assistant import CodeAssistant

class TestCodeAssistant(unittest.TestCase):
    
    @patch('requests.get')
    def test_init_connection_check(self, mock_get):
        # Setup mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"models": [{"name": "codellama:7b"}]}
        mock_get.return_value = mock_response
        
        # Test
        assistant = CodeAssistant()
        
        # Assert
        mock_get.assert_called_once_with("http://localhost:11434/api/tags")
        
    @patch('requests.post')
    def test_complete(self, mock_post):
        # Setup mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"response": "test completion"}
        mock_post.return_value = mock_response
        
        # Test
        with patch('requests.get') as mock_get:
            mock_get_response = MagicMock()
            mock_get_response.status_code = 200
            mock_get_response.json.return_value = {"models": [{"name": "codellama:7b"}]}
            mock_get.return_value = mock_get_response
            
            assistant = CodeAssistant()
            result = assistant.complete("test prompt")
        
        # Assert
        self.assertEqual(result, "test completion")
        mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()
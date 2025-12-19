import unittest
from unittest.mock import patch, Mock
from backend.ingestion import parser

class TestParser(unittest.TestCase):

    @patch('requests.get')
    def test_get_article_content_success(self, mock_get):
        # Mock the response from requests.get
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'<html><body><article><h1>Title</h1><p>Content</p></article></body></html>'
        mock_get.return_value = mock_response

        # Call the function
        article = parser.get_article_content("http://example.com")

        # Assertions
        self.assertIsNotNone(article)
        self.assertEqual(article.name, "article")
        self.assertIn("Title", article.get_text())

    @patch('requests.get')
    def test_get_article_content_no_article(self, mock_get):
        # Mock the response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'<html><body><p>No article here.</p></body></html>'
        mock_get.return_value = mock_response

        # Call the function
        article = parser.get_article_content("http://example.com")

        # Assertion
        self.assertIsNone(article)

    @patch('requests.get')
    def test_get_article_content_request_fails(self, mock_get):
        # Mock a request exception
        mock_get.side_effect = requests.exceptions.RequestException

        # Call the function
        article = parser.get_article_content("http://example.com")

        # Assertion
        self.assertIsNone(article)

if __name__ == '__main__':
    unittest.main()

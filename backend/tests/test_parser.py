import unittest
from unittest.mock import patch, Mock
from backend.ingestion.parser import parse_article_content, get_chapter_and_lesson

class TestParser(unittest.TestCase):

    @patch('requests.get')
    def test_parse_article_content(self, mock_get):
        # Mock the response from requests.get
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = """
        <html><body><article>
        <h1>Test Title</h1>
        <p>This is a paragraph.</p>
        </article></body></html>
        """
        mock_get.return_value = mock_response

        text, url, chapter, lesson = parse_article_content("http://example.com/docs/chapter1/lesson1")
        
        self.assertIn("Test Title", text)
        self.assertIn("This is a paragraph.", text)
        self.assertEqual(url, "http://example.com/docs/chapter1/lesson1")
        self.assertEqual(chapter, "chapter1")
        self.assertEqual(lesson, "lesson1")

    def test_get_chapter_and_lesson(self):
        url = "http://example.com/docs/chapter1/lesson1"
        chapter, lesson = get_chapter_and_lesson(url)
        self.assertEqual(chapter, "chapter1")
        self.assertEqual(lesson, "lesson1")
        
        url = "http://example.com/docs/another-chapter/another-lesson"
        chapter, lesson = get_chapter_and_lesson(url)
        self.assertEqual(chapter, "another-chapter")
        self.assertEqual(lesson, "another-lesson")

    @patch('requests.get')
    def test_parse_article_content_no_article(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = "<html><body><p>No article tag</p></body></html>"
        mock_get.return_value = mock_response

        result = parse_article_content("http://example.com")
        self.assertEqual(result, (None, None, None, None))

if __name__ == '__main__':
    unittest.main()

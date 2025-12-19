import unittest
from bs4 import BeautifulSoup
from backend.ingestion import chunker

class TestChunker(unittest.TestCase):

    def test_chunk_article_simple(self):
        sample_html = """
        <article>
            <p>This is a short text that should result in a single chunk.</p>
        </article>
        """
        article_tag = BeautifulSoup(sample_html, "html.parser").find("article")
        chunks = chunker.chunk_article(article_tag, chunk_size=200)
        self.assertEqual(len(chunks), 1)
        self.assertIn("single chunk", chunks[0])

    def test_chunk_article_multiple_chunks(self):
        sample_html = """
        <article>
            <h1>Title</h1>
            <p>This is the first paragraph. It is long enough to potentially be split.</p>
            <p>This is the second paragraph. Combined with the first, it should definitely exceed the chunk size.</p>
        </article>
        """
        article_tag = BeautifulSoup(sample_html, "html.parser").find("article")
        chunks = chunker.chunk_article(article_tag, chunk_size=100, overlap=10)
        self.assertGreater(len(chunks), 1)
        
    def test_chunk_article_with_overlap(self):
        sample_html = "<article><p>This is a long sentence designed to test the overlap functionality and see if the end of the first chunk appears at the beginning of the second chunk.</p></article>"
        article_tag = BeautifulSoup(sample_html, "html.parser").find("article")
        chunks = chunker.chunk_article(article_tag, chunk_size=70, overlap=20)
        self.assertEqual(len(chunks), 2)
        # Check that the end of the first chunk is in the beginning of the second
        end_of_first = chunks[0][-10:]
        self.assertIn(end_of_first.strip(), chunks[1])

if __name__ == '__main__':
    unittest.main()

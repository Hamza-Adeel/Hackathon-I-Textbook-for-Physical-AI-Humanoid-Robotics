import unittest
from backend.ingestion.chunker import chunk_text

class TestChunker(unittest.TestCase):

    def test_chunk_text(self):
        text = "This is a sentence. This is another sentence. This is a third sentence."
        chunks = chunk_text(text, max_chunk_size=30, overlap=10)
        self.assertEqual(len(chunks), 2)
        self.assertTrue(chunks[0].startswith("This is a sentence."))
        self.assertTrue(chunks[1].startswith("is another")) # Overlap

    def test_empty_text(self):
        text = ""
        chunks = chunk_text(text)
        self.assertEqual(len(chunks), 0)

    def test_small_text(self):
        text = "This is a short text."
        chunks = chunk_text(text)
        self.assertEqual(len(chunks), 1)
        self.assertEqual(chunks[0], text)

if __name__ == '__main__':
    unittest.main()

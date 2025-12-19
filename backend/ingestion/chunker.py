from bs4 import Tag
import re

def chunk_article(article: Tag, chunk_size: int = 1000, overlap: int = 100) -> list[str]:
    """
    Chunks the text content of a BeautifulSoup <article> tag.
    It splits by headings first, then paragraphs, and creates chunks
    of a target size with overlap.
    """
    chunks = []
    current_chunk = ""
    
    # Find all text blocks (paragraphs, list items, etc.)
    text_blocks = [p.get_text(strip=True) for p in article.find_all(['p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    
    for block in text_blocks:
        if not block:
            continue
            
        # If adding the next block makes the chunk too large, finalize the current chunk
        if len(current_chunk) + len(block) > chunk_size:
            chunks.append(current_chunk.strip())
            # Start the next chunk with an overlap from the end of the current one
            current_chunk = current_chunk[-overlap:] + " " + block
        else:
            current_chunk += " " + block
            
    # Add the last remaining chunk
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

if __name__ == "__main__":
    # This requires a bs4.Tag object, so we'll simulate it
    from bs4 import BeautifulSoup
    
    sample_html = """
    <article>
        <h1>Main Title</h1>
        <p>This is the first paragraph. It introduces the main topic.</p>
        <h2>Subtitle 1</h2>
        <p>This is a paragraph under the first subtitle. It contains some details.</p>
        <p>This is another paragraph. It continues the discussion.</p>
        <h2>Subtitle 2</h2>
        <p>This is a paragraph under the second subtitle. It explains a related concept. It is a bit longer to test the chunking logic and see how it splits the text into smaller pieces.</p>
    </article>
    """
    article_tag = BeautifulSoup(sample_html, "html.parser").find("article")
    
    if article_tag:
        text_chunks = chunk_article(article_tag, chunk_size=150, overlap=30)
        print(f"Generated {len(text_chunks)} chunks:")
        for i, chunk in enumerate(text_chunks):
            print(f"--- Chunk {i+1} ---")
            print(chunk)
            print()

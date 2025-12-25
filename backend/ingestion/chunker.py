import re

def chunk_text(text: str, max_chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    """
    Splits text into chunks of a maximum size, with a specified overlap.
    This is a simple implementation that splits by sentences.
    A more advanced implementation could be structure-aware (headings, paragraphs).
    """
    
    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 < max_chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            # Start new chunk with overlap
            current_chunk = current_chunk[-overlap:] + sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

if __name__ == '__main__':
    # Example usage:
    sample_text = (
        "This is the first sentence. This is the second sentence. This is the third sentence. "
        "Here is a longer fourth sentence to make the chunking more interesting. "
        "The fifth sentence will definitely push it over the edge. "
        "And a sixth one for good measure. Let's add a seventh. And an eighth. "
        "The ninth sentence is here. The tenth sentence concludes this example."
    )
    
    chunks = chunk_text(sample_text, max_chunk_size=150, overlap=50)
    
    print(f"Original text length: {len(sample_text)}")
    print(f"Number of chunks: {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} (length: {len(chunk)}) ---")
        print(chunk)

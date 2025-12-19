import logging
from urllib.parse import urlparse
from . import crawler, parser, chunker, embedding, vector_db

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = "https://hackathon-i-textbook-for-physical-a.vercel.app/"

def run_ingestion():
    """
    Runs the full content ingestion pipeline.
    """
    logging.info("Starting content ingestion process...")
    initial_count = vector_db.get_collection_count()
    logging.info(f"Initial vector count in collection: {initial_count}")


    # 1. Get all documentation URLs
    logging.info(f"Crawling for doc URLs starting from {BASE_URL}...")
    doc_urls = crawler.get_all_doc_urls(BASE_URL)
    if not doc_urls:
        logging.error("No documentation URLs found. Aborting.")
        return
    logging.info(f"Found {len(doc_urls)} documentation URLs.")

    # 2. Create Qdrant collection if it doesn't exist
    vector_db.create_collection_if_not_exists()

    # 3. Process each URL
    total_chunks_ingested = 0
    for url in doc_urls:
        logging.info(f"Processing URL: {url}")
        
        # a. Get article content
        article_tag = parser.get_article_content(url)
        if not article_tag:
            logging.warning(f"Could not extract article from {url}. Skipping.")
            continue
            
        # b. Chunk the article
        text_chunks = chunker.chunk_article(article_tag)
        if not text_chunks:
            logging.warning(f"No text chunks generated for {url}. Skipping.")
            continue
        logging.info(f"Generated {len(text_chunks)} chunks from {url}.")
            
        # c. Generate embeddings
        embeddings = embedding.get_embeddings(text_chunks)
        if not embeddings or len(embeddings) != len(text_chunks):
            logging.error(f"Failed to generate embeddings for all chunks in {url}. Skipping.")
            continue
            
        # d. Prepare metadata payloads
        path_parts = urlparse(url).path.strip('/').split('/')
        chapter = path_parts[1] if len(path_parts) > 1 else 'unknown'
        lesson = path_parts[-1] if len(path_parts) > 1 else 'unknown'
        
        payloads = [
            {
                "text": chunk,
                "source_url": url,
                "chapter": chapter,
                "lesson": lesson
            }
            for chunk in text_chunks
        ]
        
        # e. Upload to Qdrant
        vector_db.upload_vectors(vectors=embeddings, payloads=payloads)
        total_chunks_ingested += len(text_chunks)
        logging.info(f"Successfully uploaded {len(text_chunks)} vectors for {url}.")

    logging.info(f"--- Ingestion Complete ---")
    logging.info(f"Total chunks ingested in this run: {total_chunks_ingested}")

    # Sanity Check
    final_count = vector_db.get_collection_count()
    logging.info(f"Final vector count in collection: {final_count}")
    if final_count >= initial_count + total_chunks_ingested:
        logging.info("Sanity check passed: Vector count increased as expected.")
    else:
        logging.warning("Sanity check failed: Vector count did not increase as expected.")


if __name__ == "__main__":
    run_ingestion()
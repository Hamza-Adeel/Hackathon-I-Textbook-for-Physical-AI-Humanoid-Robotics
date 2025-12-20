import logging
from backend.ingestion.crawler import get_all_documentation_urls
from backend.ingestion.parser import parse_article_content
from backend.ingestion.chunker import chunk_text
from backend.ingestion.embedding import get_cohere_client, generate_embeddings
from backend.ingestion.vector_db import get_qdrant_client, create_collection_if_not_exists, upload_vectors, COLLECTION_NAME

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

START_URL = "https://hackathon-i-textbook-for-physical-a.vercel.app/"

def main():
    logging.info("Starting ingestion process...")

    # Get clients
    cohere_client = get_cohere_client()
    qdrant_client = get_qdrant_client()

    # Create collection
    create_collection_if_not_exists(qdrant_client)

    # Get URLs
    urls = get_all_documentation_urls(START_URL)

    all_chunks = []
    all_payloads = []

    for url in urls:
        text, source_url, chapter, lesson = parse_article_content(url)

        if not text:
            continue

        chunks = chunk_text(text)
        
        for chunk in chunks:
            all_chunks.append(chunk)
            all_payloads.append({
                "text": chunk,
                "source_url": source_url,
                "chapter": chapter,
                "lesson": lesson,
            })

    if not all_chunks:
        logging.info("No content to ingest.")
        return

    # Generate embeddings
    embeddings = generate_embeddings(all_chunks, cohere_client)

    if not embeddings:
        logging.error("Failed to generate embeddings. Aborting.")
        return

    # Upload to Qdrant
    upload_vectors(qdrant_client, embeddings, all_payloads)

    logging.info("Ingestion process finished.")
    
    # Sanity check
    logging.info("Performing sanity check...")
    retrieved_points = qdrant_client.retrieve(collection_name=COLLECTION_NAME, ids=[0], with_payload=True)
    logging.info("Retrieved point:")
    print(retrieved_points)


if __name__ == "__main__":
    main()

import qdrant_client
import os
from dotenv import load_dotenv
from qdrant_client.http.models import Distance, VectorParams, PointStruct
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

COLLECTION_NAME = "textbook_content"

def get_qdrant_client():
    """
    Initializes and returns the Qdrant client.
    """
    url = os.getenv("QDRANT_URL")
    api_key = os.getenv("QDRANT_API_KEY")

    if not url or not api_key:
        raise ValueError("QDRANT_URL or QDRANT_API_KEY not found in environment variables.")

    logging.info("Qdrant client initialized.")
    return qdrant_client.QdrantClient(url=url, api_key=api_key)

def create_collection_if_not_exists(client):
    """
    Creates the Qdrant collection if it doesn't already exist.
    """
    try:
        collections = client.get_collections().collections
        collection_names = [collection.name for collection in collections]

        if COLLECTION_NAME not in collection_names:
            logging.info(f"Collection '{COLLECTION_NAME}' not found. Creating collection.")
            client.recreate_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
            )
            logging.info(f"Collection '{COLLECTION_NAME}' created.")
        else:
            logging.info(f"Collection '{COLLECTION_NAME}' already exists.")

    except Exception as e:
        logging.error(f"Error creating collection: {e}")

def upload_vectors(client, vectors: list[list[float]], payloads: list[dict]):
    """
    Uploads vectors and their payloads to the Qdrant collection in batches.
    """
    if not vectors:
        return

    batch_size = 100
    num_vectors = len(vectors)
    logging.info(f"Uploading {num_vectors} vectors to collection '{COLLECTION_NAME}' in batches of {batch_size}...")

    for i in range(0, num_vectors, batch_size):
        batch_vectors = vectors[i:i + batch_size]
        batch_payloads = payloads[i:i + batch_size]
        
        points = [
            PointStruct(id=i + j, vector=vector, payload=payload)
            for j, (vector, payload) in enumerate(zip(batch_vectors, batch_payloads))
        ]
        
        try:
            client.upsert(
                collection_name=COLLECTION_NAME,
                wait=True,
                points=points,
            )
            logging.info(f"Uploaded batch {i // batch_size + 1}/{(num_vectors + batch_size - 1) // batch_size}")
        except Exception as e:
            logging.error(f"Error uploading batch: {e}")


if __name__ == '__main__':
    # Example usage:
    qdrant_client = get_qdrant_client()
    create_collection_if_not_exists(qdrant_client)

    # Example data
    sample_vectors = [[0.1] * 1024, [0.2] * 1024]
    sample_payloads = [
        {"text": "This is a sample text.", "source_url": "http://example.com/a", "chapter": "a", "lesson": "a"},
        {"text": "Another sample text.", "source_url": "http://example.com/b", "chapter": "b", "lesson": "b"},
    ]

    upload_vectors(qdrant_client, sample_vectors, sample_payloads)

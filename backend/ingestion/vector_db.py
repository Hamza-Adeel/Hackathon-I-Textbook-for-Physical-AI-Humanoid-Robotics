import qdrant_client
from qdrant_client.http import models
import os
from dotenv import load_dotenv
import uuid

# Load environment variables from .env file
load_dotenv()

qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

if not qdrant_url or not qdrant_api_key:
    raise ValueError("QDRANT_URL or QDRANT_API_KEY not found in environment variables.")

# Initialize the Qdrant client
client = qdrant_client.QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key,
)

COLLECTION_NAME = "textbook_content"
VECTOR_SIZE = 1024  # From Cohere's embed-english-v3.0

def create_collection_if_not_exists():
    """
    Creates the Qdrant collection if it doesn't already exist.
    """
    try:
        collections = client.get_collections().collections
        collection_names = [collection.name for collection in collections]
        if COLLECTION_NAME not in collection_names:
            client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE),
            )
            print(f"Collection '{COLLECTION_NAME}' created.")
        else:
            print(f"Collection '{COLLECTION_NAME}' already exists.")
    except Exception as e:
        print(f"Error creating or checking collection: {e}")


def upload_vectors(vectors: list[list[float]], payloads: list[dict]):
    """
    Uploads vectors and their metadata payloads to the Qdrant collection.
    """
    if not vectors:
        return

    points = [
        models.PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload=payload,
        )
        for vector, payload in zip(vectors, payloads)
    ]

    try:
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points,
            wait=True,
        )
    except Exception as e:
        print(f"Error uploading vectors to Qdrant: {e}")

def get_collection_count() -> int:
    """
    Returns the number of vectors in the collection.
    """
    try:
        count_result = client.count(collection_name=COLLECTION_NAME, exact=True)
        return count_result.count
    except Exception as e:
        print(f"Error getting collection count: {e}")
        return 0


if __name__ == "__main__":
    # Example usage
    print("Checking and creating Qdrant collection...")
    create_collection_if_not_exists()

    # Simulate uploading some data
    print("\nUploading dummy data...")
    dummy_vectors = [[i / 10.0 for i in range(VECTOR_SIZE)] for _ in range(2)]
    dummy_payloads = [
        {"text": "This is a dummy chunk 1.", "source_url": "http://example.com/page1", "chapter": "intro", "lesson": "dummy-data"},
        {"text": "This is a dummy chunk 2.", "source_url": "http://example.com/page2", "chapter": "intro", "lesson": "dummy-data-2"},
    ]
    
    upload_vectors(dummy_vectors, dummy_payloads)
    print("Dummy data upload finished.")

    # Verify count
    count = get_collection_count()
    print(f"\nTotal points in collection: {count}")
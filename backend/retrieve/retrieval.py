import os
from qdrant_client import QdrantClient
from dotenv import load_dotenv
from shared.embedding import get_cohere_client, generate_embeddings

load_dotenv()

# Get Qdrant credentials from environment variables
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "textbook_content"

def get_qdrant_client():
    """Returns a QdrantClient instance."""
    if not QDRANT_URL or not QDRANT_API_KEY:
        raise ValueError("QDRANT_URL and QDRANT_API_KEY must be set in the .env file.")
    
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
    )
    return client

def semantic_search(query: str, top_k: int = 5, score_threshold: float = 0.5):
    """Performs a semantic search on the Qdrant collection.

    Args:
        query: The query string.
        top_k: The number of results to return.
        score_threshold: The minimum score for a result to be returned.

    Returns:
        A list of search results.
    """
    cohere_client = get_cohere_client()
    query_vector = generate_embeddings([query], cohere_client, input_type="search_query")[0]

    client = get_qdrant_client()
    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k,
        score_threshold=score_threshold,
        with_payload=True,
    )
    return search_result

if __name__ == '__main__':
    # Example usage:
    try:
        qdrant_client = get_qdrant_client()
        print("Successfully connected to Qdrant.")
        # You can now use the client to interact with your Qdrant collection
        # For example, to get collection info:
        collection_info = qdrant_client.get_collection(collection_name=COLLECTION_NAME)
        print(f"Collection info: {collection_info}")

        # Example of semantic search
        results = semantic_search("What is ROS 2?")
        print("\nSearch results for 'What is ROS 2?':")
        for result in results:
            print(f"- Score: {result.score}")
            print(f"  ID: {result.id}")
            print(f"  Payload: {result.payload}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

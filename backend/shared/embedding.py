import cohere
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def get_cohere_client():
    """
    Initializes and returns the Cohere client.
    """
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        raise ValueError("COHERE_API_KEY not found in environment variables.")
    logging.info("Cohere client initialized.")
    return cohere.Client(api_key)


def generate_embeddings(texts: list[str], client, input_type="search_document") -> list[list[float]]:
    """
    Generates embeddings for a list of texts using the Cohere API.
    """
    if not texts:
        return []
    
    logging.info(f"Generating embeddings for {len(texts)} texts...")
    try:
        response = client.embed(
            texts=texts,
            model="embed-english-v3.0",
            input_type=input_type
        )
        logging.info("Embeddings generated successfully.")
        return response.embeddings
    except Exception as e:
        logging.error(f"Error generating embeddings: {e}")
        return []

if __name__ == '__main__':
    # Example usage:
    cohere_client = get_cohere_client()
    
    sample_texts = [
        "This is the first document.",
        "This is the second document, which is a bit longer.",
        "And the third one, for good measure."
    ]
    
    embeddings = generate_embeddings(sample_texts, cohere_client)
    
    if embeddings:
        logging.info(f"Successfully generated {len(embeddings)} embeddings.")
        for i, embedding in enumerate(embeddings):
            logging.info(f"  - Embedding {i+1} dimension: {len(embedding)}")
    else:
        logging.error("Failed to generate embeddings.")

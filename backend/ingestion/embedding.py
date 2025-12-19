import cohere
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    raise ValueError("COHERE_API_KEY not found in environment variables.")

# Initialize the Cohere client
co = cohere.Client(cohere_api_key)

def get_embeddings(texts: list[str], model: str = "embed-english-v3.0") -> list[list[float]]:
    """
    Generates embeddings for a list of texts using the Cohere API.
    """
    if not texts:
        return []
    
    try:
        response = co.embed(
            texts=texts,
            model=model,
            input_type="search_document" # Use "search_document" for texts to be stored in a vector database
        )
        return response.embeddings
    except cohere.CohereError as e:
        print(f"Cohere API error: {e}")
        # Depending on the error, you might want to handle it differently
        # For now, we'll return an empty list for simplicity
        return []

if __name__ == "__main__":
    # Example usage
    sample_texts = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?"
    ]
    
    embeddings = get_embeddings(sample_texts)
    
    if embeddings:
        print(f"Successfully generated {len(embeddings)} embeddings.")
        print(f"Dimension of the first embedding: {len(embeddings[0])}")
        # print("First embedding:", embeddings[0][:5], "...") # Print first 5 dimensions
    else:
        print("Failed to generate embeddings.")

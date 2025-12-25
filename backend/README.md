# Backend

This directory contains the backend code for the robotics textbook project.

## Modules

### Ingestion

The `ingestion` module is responsible for crawling the textbook content, parsing it, chunking it, creating embeddings, and storing them in a Qdrant vector database.

### Retrieval

The `retrieve` module is responsible for retrieving the embedded textbook content from the Qdrant vector database.

#### How it works

1.  **`retrieval.py`**:
    *   Connects to the Qdrant Cloud collection.
    *   Provides a `semantic_search` function that takes a query string and returns the top-k most relevant chunks.
    *   Uses the `sentence-transformers` library to create an embedding for the query.

2.  **`validation.py`**:
    *   Contains a list of test queries to validate the retrieval process.
    *   The `run_validation` function executes the test queries and prints the results.
    *   The validation results are logged to `validation.log`.

#### How to run validation

1.  Make sure you have a `.env` file in the `backend` directory with your Qdrant credentials:
    ```
    QDRANT_URL=<your-qdrant-url>
    QDRANT_API_KEY=<your-qdrant-api-key>
    ```
2.  Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
3.  Run the validation script:
    ```
    python retrieve/validation.py
    ```

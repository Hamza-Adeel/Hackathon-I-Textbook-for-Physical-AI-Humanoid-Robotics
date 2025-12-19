# Quickstart: Content Ingestion Script

This guide explains how to set up and run the content ingestion script for the textbook.

## 1. Prerequisites

- Python 3.11+
- An internet connection

## 2. Environment Setup

1.  **Clone the repository** and navigate to the project root.

2.  **Create a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r src/ingestion/requirements.txt
    ```

4.  **Configure environment variables**:
    - Make a copy of the `.env.example` file and name it `.env`.
    - Open the `.env` file and add your API keys and Qdrant URL:
      ```
      COHERE_API_KEY="your_cohere_api_key"
      QDRANT_URL="your_qdrant_cloud_url"
      QDRANT_API_KEY="your_qdrant_api_key"
      ```

## 3. Running the Ingestion Script

- Execute the main script from the root of the project:

  ```bash
  python -m src.ingestion.main
  ```

- The script will begin fetching, processing, and embedding the content from the Docusaurus website.
- You can monitor the progress via the console logs.

## 4. Verifying the Ingestion

- After the script completes, it will log the total number of vectors added.
- You can also log into your Qdrant Cloud dashboard to inspect the `textbook_content` collection and see the stored vectors and their metadata.

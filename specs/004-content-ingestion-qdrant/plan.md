# Implementation Plan: Content Ingestion and Vector Database Setup

**Branch**: `004-content-ingestion-qdrant` | **Date**: 2025-12-19 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/004-content-ingestion-qdrant/spec.md`

## Summary

This plan outlines the steps to create a Python script that fetches content from a Docusaurus website, extracts the text, chunks it, generates embeddings with Cohere, and stores everything in a Qdrant vector database. The goal is to make the textbook content available for semantic search.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: `requests`, `beautifulsoup4`, `cohere`, `qdrant-client`
**Storage**: Qdrant Cloud (free tier)
**Testing**: `pytest`
**Target Platform**: Backend script (OS-agnostic)
**Project Type**: Single project (backend script)
**Performance Goals**: Ingest a single page in <10 seconds on average.
**Constraints**: No FastAPI, No OpenAI, No frontend.
**Scale/Scope**: Ingest a single Docusaurus website hosted on Vercel.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Scope Alignment**: Does the feature align with the mission of writing a textbook? (Yes, it makes the textbook content searchable and more useful.)
- [x] **Stack Adherence**: Does the plan exclusively use the approved technology stack (Docusaurus, Markdown)? (The plan is for ingesting content *from* a Docusaurus site, which is compliant.)
- [x] **Beginner-Focused**: Is the proposed content and structure simple and accessible for beginners? (Yes, the plan is straightforward.)
- [x] **Deliverable-Oriented**: Does the feature contribute directly to the Docusaurus textbook? (Yes, it enhances the value of the textbook.)

## Project Structure

### Documentation (this feature)

```text
specs/004-content-ingestion-qdrant/
├── plan.md              # This file
├── research.md          # Research and key decisions
├── data-model.md        # Data schema for Qdrant
├── quickstart.md        # How to run the ingestion script
└── tasks.md             # To be created by /sp.tasks
```

### Source Code (repository root)

```text
# Single project (backend script)
src/
├── ingestion/
│   ├── __init__.py
│   ├── main.py          # Script entry point
│   ├── crawler.py       # Fetches and finds content pages
│   ├── parser.py        # Extracts and cleans text
│   ├── chunker.py       # Chunks text into sections
│   ├── embedding.py     # Generates embeddings with Cohere
│   └── vector_db.py     # Handles Qdrant operations
└── tests/
    ├── __init__.py
    ├── test_crawler.py
    ├── test_parser.py
    └── test_chunker.py

scripts/
└── run_ingestion.sh     # Convenience script

.env.example             # For API keys
```

**Structure Decision**: A single project structure is chosen, organized into modules within the `src/ingestion` directory. This is suitable for a backend script and allows for clear separation of concerns and easy testing.

## Detailed Implementation Steps

1.  **Environment Setup**:
    *   Create a `requirements.txt` file with `requests`, `beautifulsoup4`, `cohere`, `qdrant-client`, `python-dotenv`.
    *   Create a `.env.example` file for `COHERE_API_KEY` and `QDRANT_API_KEY`, `QDRANT_URL`.
2.  **Crawler (`crawler.py`)**:
    *   Implement a function to fetch and parse the `sitemap.xml` from the Vercel URL.
    *   Fall back to crawling the homepage if sitemap is not found.
    *   Filter URLs to include only those under the `/docs/` path.
    *   Return a list of valid documentation page URLs.
3.  **Parser (`parser.py`)**:
    *   Implement a function that takes a URL, fetches the HTML, and uses BeautifulSoup to find the `<article>` tag.
    *   Extract all text content from the article.
    *   Clean the text by removing extra whitespace and any remaining HTML artifacts.
4.  **Chunker (`chunker.py`)**:
    *   Implement a structure-aware chunking function that splits the cleaned text first by headings, then by paragraphs.
    *   Add a configurable overlap (e.g., 1-2 sentences) between chunks.
5.  **Embedding (`embedding.py`)**:
    *   Implement a function that initializes the Cohere client.
    -   Create a function that takes a list of text chunks and calls the `cohere.embed` API using the `embed-english-v3.0` model.
6.  **Vector DB (`vector_db.py`)**:
    *   Implement a function to initialize the Qdrant client.
    *   Create a function to create the Qdrant collection (`textbook_content`) with a vector size of 1024 and `Cosine` distance metric, if it doesn't already exist.
    *   Implement a function to upload vectors and their metadata payloads to Qdrant in batches.
    *   The metadata payload will include `text`, `source_url`, `chapter`, and `lesson`.
7.  **Main Script (`main.py`)**:
    *   Tie all the modules together in a main `run()` function.
    *   Load environment variables.
    *   Call the crawler to get URLs.
    *   Loop through URLs: parse, chunk, embed, and upload.
    *   Add logging to track progress, successes, and failures.
    *   Implement retries for network-dependent calls (fetching URLs, calling Cohere/Qdrant).
8.  **Sanity Checks**:
    *   After the script runs, log the total number of vectors added.
    *   Implement a simple check to retrieve a few sample vectors from Qdrant to ensure the data was written correctly.
9.  **Testing**:
    *   Write unit tests for the `parser` and `chunker` functions using sample HTML content.
    *   Write integration tests (if possible in a hackathon context) to test the flow with a mock web server and mock API clients.
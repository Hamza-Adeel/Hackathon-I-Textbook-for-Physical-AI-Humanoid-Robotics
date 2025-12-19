# Research & Decisions for Content Ingestion

This document outlines the key technical decisions made for the content ingestion feature.

## 1. Web Scraping Strategy

- **Decision**: Use a combination of sitemap parsing and link crawling. First, attempt to find and parse `sitemap.xml`. If not available, crawl the home page for links matching the `/docs/` path prefix.
- **Rationale**: A sitemap provides a reliable and complete list of all pages. A manual crawl is a good fallback. Filtering by `/docs/` ensures we only ingest textbook content, as requested.
- **Implementation**:
    - Use `requests` to fetch `sitemap.xml` and page HTML.
    - Use `BeautifulSoup` to parse XML and HTML.
    - For content extraction, target the `<article>` tag, which is the standard main content container in Docusaurus.

## 2. Text Chunking Strategy

- **Decision**: Implement a structure-aware chunking strategy.
- **Rationale**: The feature spec requires chunking by "meaningful sections". Splitting by semantic boundaries like headings and paragraphs is more effective for RAG than simple fixed-size chunks, as it keeps related context together.
- **Implementation**:
    - First, split the extracted HTML content by heading tags (`H1`, `H2`, `H3`, etc.).
    - Then, further split the content within each heading section by paragraphs.
    - A small overlap of 1-2 sentences will be added between chunks to preserve context.

## 3. Embedding Model

- **Decision**: Use Cohere's `embed-english-v3.0` model.
- **Rationale**: This is a powerful and recent model suitable for semantic search. The user explicitly requested Cohere.
- **Vector Dimension**: 1024.

## 4. Vector Database (Qdrant)

- **Decision**:
    - **Collection Name**: `textbook_content`
    - **Vector Size**: 1024 (to match `embed-english-v3.0`).
    - **Distance Metric**: `Cosine` similarity.
- **Rationale**: Cosine is the standard and most effective distance metric for comparing text embeddings.
- **Metadata Schema**: Each vector will include a payload with the following metadata:
    - `text`: The raw text of the content chunk.
    - `source_url`: The full URL of the page the chunk came from.
    - `chapter`: The chapter name, extracted from the URL path (e.g., `/docs/ros-2/...` -> `ros-2`).
    - `lesson`: The lesson name, extracted from the URL path (e.g., `.../understanding-nodes-topics-services` -> `understanding-nodes-topics-services`).


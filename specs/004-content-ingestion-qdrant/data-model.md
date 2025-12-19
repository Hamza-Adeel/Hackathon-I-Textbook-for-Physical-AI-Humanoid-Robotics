# Data Model: Content Ingestion

This document defines the data model for the content chunks and their metadata to be stored in the Qdrant vector database.

## Entity: Content Chunk

A `Content Chunk` represents a piece of text extracted from the source textbook, which is then vectorized and stored.

### Schema

Each vector stored in the Qdrant collection will have a corresponding metadata payload with the following schema:

| Field        | Type   | Description                                                                                             | Example                                         |
|--------------|--------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `text`       | String | The raw text content of the chunk. This is the content that gets embedded.                              | "A ROS 2 node is a fundamental component..."    |
| `source_url` | String | The full URL of the source page from which the chunk was extracted.                                     | `https://.../docs/ros-2/understanding-nodes`      |
| `chapter`    | String | The name of the chapter, derived from the first path segment after `/docs/`.                            | `ros-2`                                         |
| `lesson`     | String | The name of the lesson, derived from the last path segment of the URL.                                  | `understanding-nodes`                           |

### Qdrant Collection Details

- **Collection Name**: `textbook_content`
- **Vector Size**: `1024` (for Cohere's `embed-english-v3.0` model)
- **Distance Metric**: `Cosine`

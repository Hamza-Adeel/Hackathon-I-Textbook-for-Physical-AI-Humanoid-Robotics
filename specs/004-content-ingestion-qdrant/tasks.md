# Tasks: Content Ingestion and Vector Database Setup

**Input**: Design documents from `specs/004-content-ingestion-qdrant/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [x] T001 Create project directory structure: `backend/ingestion`, `backend/tests`, `backend/scripts`
- [x] T002 Create `backend/requirements.txt` with `requests`, `beautifulsoup4`, `cohere`, `qdrant-client`, `python-dotenv`
- [x] T003 [P] Create `.env.example` at the repository root for API keys and URLs
- [x] T004 [P] Create empty Python files with `__init__.py` in `backend/ingestion` and `backend/tests`
- [x] T005 [P] Create empty script files: `backend/ingestion/main.py`, `crawler.py`, `parser.py`, `chunker.py`, `embedding.py`, `vector_db.py`

---

## Phase 2: User Story 1 - Content Ingestion (Priority: P1) 🎯 MVP

**Goal**: Implement the end-to-end content ingestion pipeline.

**Independent Test**: Run the main script (`python -m backend.ingestion.main`) and verify that content from the source URL is successfully processed and stored in the Qdrant collection.

### Implementation for User Story 1

- [x] T006 [US1] Implement sitemap and URL fetching logic in `backend/ingestion/crawler.py`
- [x] T007 [US1] Implement HTML content extraction from `<article>` tags in `backend/ingestion/parser.py`
- [x] T008 [US1] Implement text cleaning and normalization in `backend/ingestion/parser.py`
- [x] T009 [US1] Implement structure-aware text chunking logic in `backend/ingestion/chunker.py`
- [x] T010 [P] [US1] Implement Cohere client and embedding generation in `backend/ingestion/embedding.py`
- [x] T011 [P] [US1] Implement Qdrant client and collection creation in `backend/ingestion/vector_db.py`
- [x] T012 [US1] Implement batch uploading of vectors and metadata to Qdrant in `backend/ingestion/vector_db.py`
- [x] T013 [US1] Implement the main ingestion workflow, tying all modules together in `backend/ingestion/main.py`
- [x] T014 [US1] Add comprehensive logging for all operations in all `backend/ingestion/` modules
- [x] T015 [US1] Implement error handling and retry mechanisms for network calls in `crawler.py`, `embedding.py`, and `vector_db.py`

---

## Phase 3: Polish & Validation

**Purpose**: Add tests, documentation, and final validation checks.

- [x] T016 [P] Write unit tests for `test_chunker.py` in `backend/tests/` to validate chunking logic
- [x] T017 [P] Write unit tests for `test_parser.py` in `backend/tests/` to validate text extraction
- [x] T018 Implement sanity checks in `backend/ingestion/main.py` to retrieve sample vectors after ingestion
- [x] T019 [P] Create a convenience script `backend/scripts/run_ingestion.ps1` to run the main ingestion module
- [x] T020 Final validation: run the full process as described in `quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Must be completed first.
- **User Story 1 (Phase 2)**: Depends on Setup completion.
- **Polish (Phase 3)**: Depends on User Story 1 completion.

### Task Dependencies within US1

- `T013` (main workflow) depends on all other tasks in the phase (`T006` - `T012`, `T014`, `T015`).
- `T012` (uploading) depends on `T011` (Qdrant client) and `T010` (embeddings).
- Most other tasks can be developed in parallel to some degree.

### Parallel Opportunities

- `T003`, `T004`, `T005` in Setup can be done in parallel.
- `T010` (embedding module) and `T011` (vector DB module) in US1 can be developed in parallel.
- `T016` and `T017` (unit tests) in Polish can be done in parallel.

---

## Implementation Strategy

### MVP First (Complete US1)

1.  Complete all tasks in **Phase 1: Setup**.
2.  Implement all tasks in **Phase 2: User Story 1**.
3.  **STOP and VALIDATE**: Run the script and confirm data is in Qdrant.
4.  This delivers the core value of the feature.

### Incremental Delivery

1.  The project is a single-feature script, so the MVP is the full delivery.
2.  Complete Phases 1, 2, and 3 in order for a robust and tested final script.

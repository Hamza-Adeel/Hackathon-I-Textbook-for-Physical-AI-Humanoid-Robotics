# This script runs the FastAPI application using Uvicorn.

# Activate the virtual environment
. ./.venv/Scripts/activate

# Run the FastAPI application
uvicorn backend.main:app --host 0.0.0.0 --port 8000

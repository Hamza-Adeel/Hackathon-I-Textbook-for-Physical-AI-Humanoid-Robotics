# This script runs the content ingestion process.

# Activate the virtual environment
. backend/.venv/Scripts/activate

# Run the main ingestion script
python -m backend.ingestion.main

from fastapi import FastAPI, BackgroundTasks
from backend.ingestion.ingestion_script import run_ingestion

app = FastAPI()

@app.post("/ingest")
async def ingest_data(background_tasks: BackgroundTasks):
    """
    Endpoint to trigger the content ingestion process.
    """
    background_tasks.add_task(run_ingestion)
    return {"message": "Content ingestion started in the background."}

@app.get("/")
async def root():
    return {"message": "Welcome to the ingestion API."}

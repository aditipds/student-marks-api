from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the JSON array and convert to dict {name: marks}
with open("students.json") as f:
    data = json.load(f)
    marks_db = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    # For each name, get marks or None if not found
    marks = [marks_db.get(n, None) for n in name]
    return {"marks": marks}

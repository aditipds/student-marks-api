from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins (allow GET requests from anywhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the student marks once when the app starts
with open("students.json") as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(request: Request):
    # Get all 'name' query parameters, e.g. ?name=Alice&name=Bob
    names = request.query_params.getlist("name")
    
    # Prepare marks in order of requested names, use None if name not found
    marks = [marks_data.get(name, None) for name in names]

    return {"marks": marks}

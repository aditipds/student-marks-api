import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load JSON data once at startup
with open("students.json", "r") as f:
    data = json.load(f)

# Convert list of dicts to a dict for quick lookup
marks_db = {item["name"]: item["marks"] for item in data}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    result = [marks_db.get(n, None) for n in name]
    return {"marks": result}

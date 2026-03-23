from fastapi import FastAPI
import json

app = FastAPI()

FILE = "results.json"


def load_results():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_results(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


@app.get("/")
def root():
    return {"message": "ML Dashboard API running"}


@app.get("/results")
def get_results():
    return load_results()


@app.post("/results")
def add_result(result: dict):
    data = load_results()
    data.append(result)
    save_results(data)
    return {"status": "saved"}
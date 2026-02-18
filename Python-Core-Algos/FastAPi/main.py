from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def hello_world():
  msg = json.loads('{"Hello":"Wrld"}')
  return msg

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
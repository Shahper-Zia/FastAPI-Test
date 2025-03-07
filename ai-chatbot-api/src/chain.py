import requests
import redis
from fastapi import FastAPI

rd = redis.Redis(host='localhost', port=6379, db=0)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    cache = rd.get(item_id)
    if cache:
        print("cache hit")
        return {"item_id": item_id, "q": q, "cache": cache}
    else:
        print("cache miss")
        rd.set(item_id, q)
        return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
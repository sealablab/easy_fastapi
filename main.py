import uvicorn 
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
        return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

## Main()
## Spin up a uvicorn Config, apply it to a uvicorn Server, tell it to run
if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

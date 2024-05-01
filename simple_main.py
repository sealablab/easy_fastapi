from fastapi import FastAPI
from pydantic import BaseModel, Field
from loguru import logger
app = FastAPI()


class Item(BaseModel):
    id: int = 0
    description: str  = 'none'

@app.get("/")
async def root():
    m = Item()
    logger.info(f"{m}")
    return m

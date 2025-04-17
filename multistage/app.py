from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging
import time

app = FastAPI()

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app-logger")

# Middleware to log request and response
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    
    response = await call_next(request)

    duration = time.time() - start_time
    logger.info(
        f"Completed response: {response.status_code} for {request.method} {request.url.path} in {duration:.4f}s"
    )

    return response

# Pydantic model for item
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Dynamic route
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

# POST route to create an item
@app.post("/items/")
def create_item(item: Item):
    return {"item_created": item}

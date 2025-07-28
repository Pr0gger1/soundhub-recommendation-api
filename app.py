import uvicorn
from fastapi import APIRouter, FastAPI

from api.controllers import routes
from api.exceptions import exception_handlers
from context import lifespan

app = FastAPI(version='1.1', lifespan = lifespan)
router = APIRouter()


def include_routers():
    for route in routes:
        router.include_router(route)

def include_error_handlers():
    for handler in exception_handlers:
        app.add_exception_handler(handler['exception'], handler['handler'])

include_routers()
include_error_handlers()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8888, reload=True)
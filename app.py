import uvicorn
from fastapi import FastAPI

from api.controllers import routes
from api.handlers import error_handlers

app = FastAPI(version='1.1')

def include_routers():
    for route in routes:
        app.include_router(route)

def add_exception_handlers():
    for exception, handler in error_handlers:
        app.add_exception_handler(exception, handler)


include_routers()
add_exception_handlers()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8888, reload=True)
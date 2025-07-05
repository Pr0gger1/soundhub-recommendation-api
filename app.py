import uvicorn
from fastapi import FastAPI

from api.controllers import routes

app = FastAPI(version='1.1')

def include_routers():
    for route in routes:
        app.include_router(route)

include_routers()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8888, reload=True)
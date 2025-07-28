from contextlib import asynccontextmanager
from threading import Thread

from fastapi import FastAPI

from api.utils.di import DependencyInjector

@asynccontextmanager
async def lifespan(app: FastAPI):
	kafka_service = DependencyInjector.get_kafka_service()

	thread = Thread(target=kafka_service.consume, daemon=True)
	thread.start()
 
	yield
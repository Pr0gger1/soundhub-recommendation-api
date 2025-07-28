from .HealthcheckController import router as healthcheck_router

routes = [healthcheck_router]

__all__ = ['routes']
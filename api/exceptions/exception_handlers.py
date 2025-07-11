from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import OperationalError

from api.exceptions.UserNotFoundException import UserNotFoundException

async def user_not_found_exception_handler(request: Request, e: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "code": 404,
            "detail": e.message
        },
    )

async def missing_env_variable_error(request: Request, e: KeyError):
    return JSONResponse(
        status_code=503,
        content={
            "code": 503,
            "detail": repr(e)
        }
    )

async def db_connection_error(request: Request, e: OperationalError):
    return JSONResponse(
        status_code=500,
        content={
            "code": 500,
            "detail": repr(e)
        }
    )

exception_handlers = [
    {
        'handler': user_not_found_exception_handler,
        'exception': UserNotFoundException
    },
    {
        'handler': missing_env_variable_error,
        'exception': KeyError
    },
    {
        'handler': db_connection_error,
        'exception': OperationalError
    }
]

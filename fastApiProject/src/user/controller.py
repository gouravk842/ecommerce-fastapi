import fastapi

from fastapi import Depends
from pymongo.database import Database
from starlette.requests import Request

from src.common_utility.response_structure import send_response
from src.user.model import User
from src.user.service import add_user_service

user_router = fastapi.APIRouter()


def get_database(request: Request):
    return request.app.db


@user_router.post("/user", response_model=User)
def create_user(user: User, db: Database = Depends(get_database)):
    status_code, message = add_user_service(db, user.dict())

    if status_code == 400:
        return send_response(status_code=status_code, error=message)

    return send_response(data=message)

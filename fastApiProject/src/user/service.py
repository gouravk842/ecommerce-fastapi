from pymongo.database import Database

from src.ecommerce.constant import USER_COLLECTION


def add_user_service(db: Database, user):
    existing_user = db[USER_COLLECTION].find_one({"email": user.get("email")})
    if existing_user:
        return 400, "User with this email already exists"

    saved_instance = db[USER_COLLECTION].insert_one(user)

    message = {
        "status": "success",
        "message": "User created successfully",
        "user_id": str(saved_instance.inserted_id)
    }

    return 200, message


def validate_user_exists(db: Database, user_id):
    user = db[USER_COLLECTION].find_one({"id": user_id})
    return user is not None

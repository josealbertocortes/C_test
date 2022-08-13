from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from datetime import timezone, datetime
import jwt
from app.server.database import (
    add_user,
    get_user,
    getNewToken
)
from app.server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UserUpdateToken,
)

router = APIRouter()

@router.post("/", response_description="user data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    token = jwt.encode({"name":user["name"],"exp": datetime.now(tz=timezone.utc)}, "secret")
    user["token"]=token
    new_user = await add_user(user)
    return ResponseModel(new_user, "user added successfully.")

@router.get("/{id}", response_description="user data retrieved")
async def get_user_data(id):
    user = await get_user(id)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")

@router.put("/{id}")
async def ge_new_token(id: str, req: UserUpdateToken = Body(...)):
    req  = jsonable_encoder(req)
    updated_user = await getNewToken(id, req)
    if updated_user:
        return ResponseModel(
            {"token":updated_user["token"]},
            "new token "
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )
from bson.objectid import ObjectId
import motor.motor_asyncio
from datetime import timezone, datetime
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
url_conexion= os.getenv('URLCONEXIONMONGO')
MONGO_DETAILS = url_conexion

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)


database = client.user

user_collection = database.get_collection("user_colection")


# helpers
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"],
        "token":user["token"]
    }



# Add a new student into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Retrieve a student with a matching ID
async def get_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


# Update a student with a matching ID
async def getNewToken(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        if user["password"]==data["password"]:
            token = jwt.encode({"name":user["name"],"exp": datetime.now(tz=timezone.utc)}, "secret")
            newToken ={"token":token}
            updated_user = await user_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": newToken}
            )
            if updated_user:
                user["token"] = token
                return user_helper(user)
            
            else:
                False 
        else:
            return False
    else:
        False



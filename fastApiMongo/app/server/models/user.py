from typing import Optional

from pydantic import BaseModel, EmailStr, Field,SecretStr


class UserSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password:SecretStr=Field(...)
    age:int=Field(...)
    token:Optional["str"]

    class Config:
 
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password":"12345",
                "age": 25,
       
            }
        }

    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value() if v else None,

        }
       


class UserUpdateToken(BaseModel):
    email: EmailStr = Field(...)
    password:SecretStr=Field(...)


    class Config:
        schema_extra = {
            "example": {
                "email": "jdoe@x.edu.ng",
                "password": "password",

            }
        }
        
    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value() if v else None,

        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
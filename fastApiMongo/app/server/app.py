from fastapi import FastAPI

from app.server.routes.user import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["users"], prefix="/users")



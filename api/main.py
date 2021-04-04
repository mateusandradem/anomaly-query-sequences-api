from fastapi import FastAPI

from api.endpoints.router import api_router

app = FastAPI()

app.include_router(api_router)

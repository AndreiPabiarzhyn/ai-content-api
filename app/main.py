from fastapi import FastAPI
from app.routes.main_routes import router

app = FastAPI()

app.include_router(router)

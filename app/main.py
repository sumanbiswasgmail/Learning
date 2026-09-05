from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Learning")

app.include_router(router)

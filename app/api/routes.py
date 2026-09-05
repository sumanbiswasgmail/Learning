import getpass

from fastapi import APIRouter

from app.services.greeting import greet

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": greet(getpass.getuser())}


@router.get("/greet/{name}")
def read_greet(name: str):
    return {"message": greet(name)}

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from .routers import patients

app = FastAPI()

app.include_router(patients.router)
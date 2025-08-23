from typing import Union
from fastapi import FastAPI, Request
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from .routers import patients

app = FastAPI()

app.include_router(patients.router)

# serves wesite on url/index.html
# TODO: serve through reverse proxy, redirect to the index.html
app.mount('/', StaticFiles(directory="public", html=True), name="static")
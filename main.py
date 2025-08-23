from typing import Union
from fastapi import FastAPI, Request
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from .routers import authrouter,patients, resources, server_events
from .lib.database_handler import DatabaseHandler

app = FastAPI()

app.include_router(authrouter.router)
app.include_router(patients.router)
app.include_router(resources.router)
app.include_router(server_events.router)


# serves wesite on url/index.html
# TODO: serve through reverse proxy, redirect to the index.html
app.mount('/', StaticFiles(directory="public", html=True), name="static")

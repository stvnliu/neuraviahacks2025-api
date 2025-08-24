from fastapi import Query, Depends, FastAPI
from sqlmodel import SQLModel, create_engine, select, Field
from datetime import datetime
from pydantic import BaseModel

class User(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True )
    UserName:str = Field(nullable=False)
    PasswordHash: str = Field(nullable=False)
    FirstName:str = Field(nullable=False)
    LastName:str = Field(nullable=False)    
    Age:int = Field(nullable=False)

class HealthRecord(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    UserName: str = Field(nullable=False)
    Height: float = Field(nullable=False)
    Weight: float = Field(nullable=False)
    Timestamp: datetime = Field(nullable=False)

class AuthTable(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    UserID:int = Field(nullable=False)
    Token:str = Field(nullable=False)
    ExpiryTimestamp:datetime = Field(nullable=False)

class Profile(BaseModel):
    username: str
    first_name: str
    last_name: str
    token: str
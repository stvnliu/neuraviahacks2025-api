from fastapi import Query, Depends, FastAPI
from sqlmodel import SQLModel, create_engine, select, Field
from datetime import datetime

class User(SQLModel):
    UserID:str = Field(nullable=False, primary_key=True )
    FirstName:str = Field(nullable=False)
    LastName:str = Field(nullable=False)    
    Age:int = Field(nullable=False)    

class HealthRecord(SQLModel, table=True):
    HealthRecordID: str = Field(nullable=False, primary_key=True)
    UserID: str = Field(nullable=False)
    Height: int = Field(nullable=False)
    Weight: int = Field(nullable=False)
    Timestamp: datetime = Field(nullable=False)
    
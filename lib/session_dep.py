from sqlmodel import Field, Session, create_engine, select
from fastapi import Depends 
from typing import Annotated

STATEMENTS = {
    'get_useer_where_id_match': 'SELECT * FROM',
    'get_all_records_where_match': 'SELECT * FROM health_records WHERE UserID = $USER$'
}
db_url = f"mysql://localhost:3306/"
connect_args = {"check_same_thread": False}
engine = create_engine(url=db_url, connect_args=connect_args)
conn = engine.connect()

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
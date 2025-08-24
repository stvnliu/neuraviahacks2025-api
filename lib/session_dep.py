import os
from typing import Annotated

from fastapi import Depends
from sqlmodel import Field, Session, create_engine, select

STATEMENTS = {
    "get_useer_where_id_match": "SELECT * FROM",
    "get_all_records_where_match": "SELECT * FROM health_records WHERE UserID = $USER$",
}
db_url = os.environ["DATABASE_URL"]
engine = create_engine(url=db_url)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

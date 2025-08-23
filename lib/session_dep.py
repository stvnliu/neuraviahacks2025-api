from sqlmodel import Field, Session, create_engine, select
from fastapi import Depends 
from typing import Annotated

STATEMENTS = {
    'get_useer_where_id_match': 'SELECT * FROM',
    'get_all_records_where_match': 'SELECT * FROM health_records WHERE UserID = $USER$'
}
db_url = f"mysql://health_dash:health_pwd@localhost/health_dash"
engine = create_engine(url=db_url)
conn = engine.connect()

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
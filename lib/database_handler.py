from .session_dep import engine, SessionDep
from sqlmodel import SQLModel, select
from ..models import User, HealthRecord
from fastapi import HTTPException, status

class DatabaseHandler:
    def init_db_tables():
        SQLModel.metadata.create_all(engine)

    def get_health_record(id:int, session:SessionDep) -> HealthRecord:
        return session.get(HealthRecord, id)

    def get_user(id:int, session:SessionDep) -> User:
        return session.get(User, id)

    def get_user_by_name(username:str, session:SessionDep) -> User|None:
        statement = select(User).where(User.UserName == username)
        result = session.exec(statement).first()
        return result

    def add_user(data: User, session:SessionDep) -> bool:
        try:
            session.add(data)
            session.commit()
            session.refresh(data)
            return True
        except:
            return False

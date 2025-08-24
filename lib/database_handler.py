from .session_dep import engine, SessionDep
from sqlmodel import SQLModel, select
from ..models import User, HealthRecord, AuthTable
from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError



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
    def verify_token(token: str, userId: str, session: SessionDep) -> bool:
        result = session.exec(select(AuthTable).where(AuthTable.UserID == userId)).first()
        print(result)
        if result != None and result.Token == token and result.ExpiryTimestamp > datetime.now():
            return True
        return False
    def put_token(body: AuthTable, session: SessionDep) -> bool:
        try:
            print("Storing token..")
            session.add(body)
            session.commit()
            session.refresh(body)
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print("failed with %s", e)
            return False
    def add_user(data: User, session:SessionDep) -> bool:
        try:
            session.add(data)
            session.commit()
            session.refresh(data)
            return True
        except:
            return False

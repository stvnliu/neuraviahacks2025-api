import string
from hashlib import sha256
import random
from datetime import datetime, timedelta
from ..models import AuthTable
from .database_handler import DatabaseHandler
from .session_dep import SessionDep
from uuid import uuid4



class AuthUtils:
    def new_token(username: str, session: SessionDep) -> AuthTable | None:
        user = DatabaseHandler.get_user_by_name(username, session)
        if user == None:
            print("something went wrong")
            return None
        expiry_date = datetime.fromtimestamp((datetime.now() 
            + timedelta(hours=1)).timestamp())
        return AuthTable(UserID=user.id, Token=str(uuid4()), ExpiryTimestamp=expiry_date)
    def verify_token(token: str, username: str, session: SessionDep) -> bool:
        return DatabaseHandler.verify_token(token, DatabaseHandler.get_user_by_name(username, session).id, session)

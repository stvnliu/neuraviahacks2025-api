from fastapi import APIRouter, status, HTTPException
from ..lib.session_dep import SessionDep;
from ..models import User
from ..lib.database_handler import DatabaseHandler
from ..models import Profile


router = APIRouter(prefix="/auth")

@router.post("/login")
def authenticate(username:str, password_hash:str, session: SessionDep) -> Profile:
    result = DatabaseHandler.get_user_by_name(username, session)
    if result is None: return HTTPException(status.HTTP_404_NOT_FOUND, "User not found!")
    user: User = result
    if user.PasswordHash != password_hash: return HTTPException(status.HTTP_403_FORBIDDEN, "password incorrect!")
    else:
        return Profile(username=user.UserName, first_name=user.FirstName, last_name=user.LastName)


@router.post("/register")
def register(user: User, session: SessionDep):
    if(DatabaseHandler.add_user(user,session)):
        return status.HTTP_200_OK
    raise HTTPException(status.HTTP_400_BAD_REQUEST,f"User data not valid!")
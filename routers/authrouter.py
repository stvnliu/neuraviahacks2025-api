from fastapi import APIRouter, status, HTTPException
from ..lib.session_dep import SessionDep;
from ..models import User
from ..lib.database_handler import DatabaseHandler
from ..models import Profile
from ..lib.auth import AuthUtils


router = APIRouter(prefix="/auth")
@router.post("/login/token")
def auth_by_token(username: str, token: str, session: SessionDep) -> Profile:
    user = DatabaseHandler.get_user_by_name(username, session)
    if user is None: 
        # print("user not found")
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    if not DatabaseHandler.verify_token(token, user.id, session):
        # print("token verification failed")
        raise HTTPException(status.HTTP_403_FORBIDDEN)
    # print(user)
    return Profile(username=user.UserName, first_name=user.FirstName, last_name=user.LastName, token=token)
@router.post("/login")
def authenticate(username:str, password_hash:str, session: SessionDep) -> Profile:
    result = DatabaseHandler.get_user_by_name(username, session)
    if result is None: raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found!")
    user: User = result
    if user.PasswordHash != password_hash: 
        raise HTTPException(status.HTTP_403_FORBIDDEN, "password incorrect!")
    else:
        t = AuthUtils.new_token(user.UserName, session)
        if t is None: 
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "problem with auth token registration.")
        if not DatabaseHandler.put_token(t, session):
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "problem with database insertion")
        return Profile(username=user.UserName, first_name=user.FirstName, last_name=user.LastName, token=t.Token, age=user.Age)


@router.post("/register")
def register(user: User, session: SessionDep):
    # TODO prevent registering same username
    if(DatabaseHandler.add_user(user,session)):
        return status.HTTP_200_OK
    raise HTTPException(status.HTTP_400_BAD_REQUEST,f"User data not valid!")
import string
from hashlib import sha256
import random
from datetime import datetime, timedelta
LENGTH=16
# All lowercase, uppercase, and digits
ALPHANUMERIC = list(string.ascii_letters + string.digits)

def __gen_token(length: int = LENGTH) -> str:
    builder = ""
    for _ in range(length):
        builder += random.choice(ALPHANUMERIC)
    return builder


class AuthBody:
    def __init__(self, token: str, until_timestamp: int):
        self.token = token
        self.until_timestamp = until_timestamp


class AuthUtils:
    def get_token() -> AuthBody:
        expiry_date = int(( 
            datetime.now() 
            + timedelta(hours=1))
            .timestamp())
        return AuthBody( __gen_token(), expiry_date)
    
    # def get_hash(data:str) -> str:
    #     return sha256(data.encode('utf-8')).hexdigest()

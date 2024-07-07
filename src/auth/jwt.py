import jwt
from datetime import datetime, timedelta
from typing import Dict, Union
from UReader.src.auth.auth import JWTInterface


PRIVATE_KEY = ""
PUBLIC_KEY = ""
ALGORITHM = "RS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_ACCESS_DAYS = 7


class JWTHandler(JWTInterface):
    def create_access_token(self, data: Dict[str, Union[str, int]]) -> str:
        to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire.isoformat()})
        encoded_jwt = jwt.encode(to_encode, PRIVATE_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def create_refresh_token(self, data: Dict[str, Union[str, int]]) -> str:
        to_encode = data.copy()
        expire = datetime.now() + timedelta(days=REFRESH_TOKEN_ACCESS_DAYS)
        to_encode.update({"exp": expire.isoformat()})
        encoded_jwt = jwt.encode(to_encode, PRIVATE_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def decode_access_token(self, token: str) -> Dict[str, Union[str, int]]:
        try:
            payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return {'error': "Token has expired"}
        except jwt.InvalidTokenError:
            return {'error': "Invalid token"}

    def get_token_expiry(self, token: str) -> datetime:
        try:
            payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
            exp = payload.get("exp")
            if exp is None:
                raise jwt.InvalidTokenError("Expiration time (exp) claim missing")
            return datetime.fromisoformat(exp)
        except jwt.InvalidTokenError:
            return datetime.min

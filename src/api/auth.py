from UReader.src.services.users import UserService
from UReader.src.schemas.users import UserSignUp,UserSignIn
from typing import Any


async def sign_up(sign_up: UserSignUp, user: UserService) -> Any:
    try:
        created_user =(
            username = sign_up.
        )
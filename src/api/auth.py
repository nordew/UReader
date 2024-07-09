from src.schemas.users import UserSchemaSignUp, UserSchemaSignIn
from src.services.users import UserService
from typing import Any


async def sign_up(user_service: UserService, sign_up: UserSchemaSignUp) -> Any:
    tokens = UserService.sign_up(user_service, sign_up)
    return tokens


async def sign_in(user_service: UserService, sign_in: UserSchemaSignIn) -> Any:
    tokens = UserService.sign_in(user_service, sign_in)
    return tokens

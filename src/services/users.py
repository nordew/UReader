from typing import List, Optional, Dict
from src.repositories.users import UserInterface
from src.schemas.users import UserSchema, UserSchemaCreate, UserSchemaUpdate, UserSchemaSignUp, UserSchemaSignIn
from src.auth.jwt import JWTHandler
import bcrypt


class UserService:
    def __init__(self, user_repositories: UserInterface):
        self.user_repositories = user_repositories

    def get_user_by_id(self, user_id: int) -> Optional[UserSchema]:
        return self.user_repositories.get_user_by_id(user_id)

    def get_user_by_email(self, email: str) -> Optional[UserSchema]:
        return self.user_repositories.get_user_by_email(email)

    def get_users(self) -> List[UserSchema]:
        return self.user_repositories.get_users()

    def create_user(self, user_create: UserSchemaCreate) -> None:
        return self.user_repositories.create_user(user_create.to_model())

    def update_user(self, user_id: int, user_update: UserSchemaUpdate) -> None:
        return self.user_repositories.update_user(user_id, user_update.update_model())

    def delete_user(self, user_id: int) -> None:
        return self.user_repositories.delete_user(user_id)

    def sign_up(self, user_data: UserSchemaSignUp) -> Dict[str, str]:
        existing_user = self.get_user_by_email(user_data.email)
        if existing_user:
            pass

        hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = UserSchemaCreate(
            username=user_data.username,
            email=user_data.email,
            avatar_filename=user_data.avatar_filename,
            password_hash=hashed_password,
            role='user',
            refresh_token=None
        )
        created_user = self.user_repositories.create_user(new_user.to_model())
        access_token = JWTHandler.create_access_token(data={'sub': new_user.username})
        refresh_token = JWTHandler.create_refresh_token(data={'sub': new_user.username})
        token_dict = {'access': access_token, 'refresh': refresh_token}
        return token_dict

    def sign_in(self, user_data: UserSchemaSignIn) -> Dict[str, str]:
        user = self.user_repositories.get_user_by_email(user_data.email)
        if not user or not bcrypt.checkpw(user_data.password.encode('utf-8'), user.password_hash.encode('utf-8')):
            pass
        access_token = JWTHandler.create_access_token(data={'sub': user.username})
        refresh_token = JWTHandler.create_refresh_token(data={'sub': user.username})
        token_dict = {'access': access_token, 'refresh': refresh_token}
        return token_dict


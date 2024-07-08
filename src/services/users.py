from typing import List, Optional
from UReader.src.models.users import Users
from UReader.src.repositories.users import UserInterface, UserCreate, UserUpdate
import bcrypt


class UserService:
    def __init__(self, user_repositories: UserInterface):
        self.user_repositories = user_repositories

    def get_user_by_id(self, user_id: int) -> Optional[Users]:
        return self.user_repositories.get_user_by_id(user_id)

    def get_user_by_email(self, email: str) -> Optional[Users]:
        return self.user_repositories.get_user_by_email(email)

    def get_users(self) -> List[Users]:
        return self.user_repositories.get_users()

    def create_user(self, user_create: UserCreate) -> Users:
        return self.user_repositories.create_user(user_create)

    def update_user(self, user_id: int, user_update: UserUpdate) -> Users:
        return self.user_repositories.update_user(user_id, user_update)

    def delete_user(self, user_id: int) -> Users:
        return self.user_repositories.delete_user(user_id)

    def sign_up(self, username: str, email: str, password: str, avatar_filename: Optional[str] = None) -> Users:
        existing_user = self.get_user_by_email(email)
        if existing_user:
            pass  #exeption UserAlreadyExist

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = Users(
            username=username,
            email=email,
            avatar_filename=avatar_filename,
            password_hash=hashed_password,
            role='user',
            refresh_token=None
        )
        created_user = self.create_user(new_user)
        return created_user

    def sign_in(self, email: str, password: str) -> Users:

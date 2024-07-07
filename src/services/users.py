from typing import List, Optional
from UReader.src.models.users import Users
from UReader.src.repositories.users import UserInterface, UserCreate, UserUpdate


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



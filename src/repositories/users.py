from typing import Optional, List
from UReader.src.models.users import Users


class UserInterface:
    def get_user_by_id(self, user_id: int) -> Optional[Users]:
        raise NotImplementedError

    def get_user_by_email(self, email: str) -> Optional[Users]:
        raise NotImplementedError

    def get_users(self, skip: int = 0, limit: int = 10) -> List[Users]:
        raise NotImplementedError

    def create_user(self, user: Users) -> Users:
        raise NotImplementedError

    def update_user(self, user_id: int, user: Users) -> Users:
        raise NotImplementedError

    def delete_user(self, user_id: int) -> Users:
        raise NotImplementedError

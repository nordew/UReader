from typing import Optional, List
from UReader.src.models.users import Users
from abc import abstractmethod
from UReader.src.schemas.users import UserCreate, UserUpdate


class UserInterface:

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[Users]:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[Users]:
        raise NotImplementedError

    @abstractmethod
    def get_users(self, skip: int = 0, limit: int = 10) -> List[Users]:
        raise NotImplementedError

    @abstractmethod
    def create_user(self, user: UserCreate) -> Users:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user_id: int, user: UserUpdate) -> Users:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user_id: int) -> Users:
        raise NotImplementedError

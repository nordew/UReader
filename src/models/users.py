from dataclasses import dataclass, field
from typing import Optional
import re
from hashlib import sha256


@dataclass
class User:
    id: int
    username: str
    email: str
    avatar_filename: Optional[str]
    password_hash: str = field(repr=False)
    role: int = 0
    refresh_token: Optional[str] = None

    ROLE_USER = 0
    ROLE_ADMIN = 1

    def __repr__(self) -> str:
        return (f"User(id={self.id}, username='{self.username}', email='{self.email}', "
                f"avatar_filename='{self.avatar_filename}', role={self.role})")

    def __str__(self) -> str:
        return f"User(username='{self.username}', email='{self.email}')"

    def check_password(self, password: str) -> bool:
        return self.password_hash == sha256(password.encode()).hexdigest()


@dataclass
class UserSignUp:
    username: str
    email: str
    password: str
    avatar_filename: Optional[str] = None

    def is_valid(self) -> bool:
        return (
            self._is_valid_username(self.username) and
            self._is_valid_email(self.email) and
            self._is_valid_password(self.password)
        )

    @staticmethod
    def _is_valid_username(username: str) -> bool:
        return isinstance(username, str) and 4 <= len(username) <= 20

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        return isinstance(email, str) and re.match(r"[^@]+@[^@]+\.[^@]+", email)

    @staticmethod
    def _is_valid_password(password: str) -> bool:
        return isinstance(password, str) and len(password) >= 6

    def hashed_password(self) -> str:
        return sha256(self.password.encode()).hexdigest()


@dataclass
class UserSignIn:
    email: str
    password: str

    def is_valid(self) -> bool:
        return (
            self._is_valid_email(self.email) and
            self._is_valid_password(self.password)
        )

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        return isinstance(email, str) and re.match(r"[^@]+@[^@]+\.[^@]+", email)

    @staticmethod
    def _is_valid_password(password: str) -> bool:
        return isinstance(password, str) and len(password) >= 6

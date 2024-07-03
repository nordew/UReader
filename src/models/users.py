class Users:
    ROLE_USER = 0
    ROLE_ADMIN = 1

    def __init__(self, id: int, username: str, email: str, avatar_filename: str,
                 password_hash: str, role: int, refresh_token: str):
        self.id = id
        self.username = username
        self.email = email
        self.avatar_filename = avatar_filename
        self.password_hash = password_hash
        self.role = role
        self.refresh_token = refresh_token

    def __repr__(self):
        return (f"User {self.id}, username {self.username}, email {self.email}, "
                f"avatar_filename {self.avatar_filename}, password_hash {self.password_hash}, "
                f"role {self.role}, refresh_token {self.refresh_token}")

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"


class UserSignUp:
    def __init__(self, username: str, email: str, password: str, avatar_filename: str = None):
        self.username = username
        self.email = email
        self.password = password
        self.avatar_filename = avatar_filename

    def is_valid(self):
        return (
            self._is_valid_username(self.username) and
            self._is_valid_email(self.email) and
            self._is_valid_password(self.password)
        )

    @staticmethod
    def _is_valid_username(username):
        return isinstance(username, str) and 4 <= len(username) <= 20

    @staticmethod
    def _is_valid_email(email):
        return isinstance(email, str) and "@" in email

    @staticmethod
    def _is_valid_password(password):
        return isinstance(password, str) and len(password) >= 6


class UserSignIn:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def is_valid(self):
        return (
            self._is_valid_email(self.email) and
            self._is_valid_password(self.password)
        )

    @staticmethod
    def _is_valid_email(email):
        return isinstance(email, str) and "@" in email

    @staticmethod
    def _is_valid_password(password):
        return isinstance(password, str) and len(password) >= 6

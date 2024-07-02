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

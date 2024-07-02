class Users:
    def __init__(self, id: int, username: str, email: str, avatar_filename: str,
                 password_hash: str, role: int, refresh_token: str):
        self.id = id
        self.username = username
        self.email = email
        self.avatar_filename = avatar_filename
        self.password_hash = password_hash
        self.role = role
        self.refresh_token = refresh_token

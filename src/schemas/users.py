from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    avatar_filename: str
    password_hash: str
    role: str = "user"
    refresh_token: str

    class Config:
        from_attributes = True

    def __repr__(self):
        return (f"User {self.id}, username {self.username}, email {self.email}, "
                f"avatar_filename {self.avatar_filename}, password_hash {self.password_hash}, "
                f"role {self.role}, refresh_token {self.refresh_token}")

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    avatar_filename: str = Field(default=None)
    password_hash: str
    role: str = "user"
    refresh_token: str

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    username: str = Field(default=None, min_length=4, max_length=20)
    email: EmailStr = Field(default=None)
    avatar_filename: str = Field(default=None)
    password: str = Field(default=None, min_length=6)
    role: str = Field(default=None)
    refresh_token: str = Field(default=None)

    class Config:
        from_attributes = True


class UserToken(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True


class UserSignUp(BaseModel):
    username: str = Field(..., min_length=4, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=6)
    avatar_filename: str = Field(default=None)

    class Config:
        from_attributes = True


class UserSignIn(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)

    class Config:
        from_attributes = True

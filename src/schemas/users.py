from pydantic import BaseModel, EmailStr, Field
from src.models.users import Users, UserSignUp, UserSignIn


class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    avatar_filename: str
    password_hash: str
    role: int
    refresh_token: str

    class Config:
        from_attributes = True

    @classmethod
    def from_model(cls, user: Users):
        return cls(
            id=user.id,
            username=user.username,
            email=user.email,
            avatar_filename=user.avatar_filename,
            password_hash=user.password_hash,
            role=user.role,
            refresh_token=user.refresh_token
        )

    def to_model(self) -> Users:
        return Users(
            id=self.id,
            username=self.username,
            email=self.email,
            avatar_filename=self.avatar_filename,
            password_hash=self.password_hash,
            role=self.role,
            refresh_token=self.refresh_token
        )

    def __repr__(self):
        return (f"User {self.id}, username {self.username}, email {self.email}, "
                f"avatar_filename {self.avatar_filename}, password_hash {self.password_hash}, "
                f"role {self.role}, refresh_token {self.refresh_token}")

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"


class UserSchemaCreate(BaseModel):
    username: str
    email: EmailStr
    avatar_filename: str = Field(default=None)
    password_hash: str
    role: int = Users.ROLE_USER
    refresh_token: str

    class Config:
        from_attributes = True

    def to_model(self) -> Users:
        return Users(
            id=0,
            username=self.username,
            email=self.email,
            avatar_filename=self.avatar_filename,
            password_hash=self.password_hash,
            role=self.role,
            refresh_token=self.refresh_token
        )


class UserSchemaUpdate(BaseModel):
    username: str = Field(default=None, min_length=4, max_length=20)
    email: EmailStr = Field(default=None)
    avatar_filename: str = Field(default=None)
    password: str = Field(default=None, min_length=6)
    role: int = Field(default=None)
    refresh_token: str = Field(default=None)

    class Config:
        from_attributes = True

    def update_model(self, user: Users) -> Users:
        if self.username is not None:
            user.username = self.username
        if self.email is not None:
            user.email = self.email
        if self.avatar_filename is not None:
            user.avatar_filename = self.avatar_filename
        if self.password is not None:
            user.password_hash = self.password
        if self.role is not None:
            user.role = self.role
        if self.refresh_token is not None:
            user.refresh_token = self.refresh_token
        return user


class UserSchemaToken(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True


class UserSchemaSignUp(BaseModel):
    username: str = Field(..., min_length=4, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=6)
    avatar_filename: str = Field(default=None)

    class Config:
        from_attributes = True

    def to_model(self) -> UserSignUp:
        return UserSignUp(
            username=self.username,
            email=self.email,
            password=self.password,
            avatar_filename=self.avatar_filename
        )


class UserSchemaSignIn(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)

    class Config:
        from_attributes = True

    def to_model(self) -> UserSignIn:
        return UserSignIn(
            email=self.email,
            password=self.password
        )
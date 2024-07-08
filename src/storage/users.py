from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.users import User as UserModel
from src.schemas.users import UserSchema
from src.repositories.users import UserInterface

# Custom errors
class UserError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class UserNotFoundError(UserError):
    def __init__(self, user_id: int):
        super().__init__(f"User with id {user_id} not found")

class EmailNotFoundError(UserError):
    def __init__(self, email: str):
        super().__init__(f"User with email {email} not found")


class UserStorage(UserInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int) -> Optional[UserSchema]:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise UserNotFoundError(user_id)
        return UserSchema.from_orm(user)

    def get_user_by_email(self, email: str) -> Optional[UserSchema]:
        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if user is None:
            raise EmailNotFoundError(email)
        return UserSchema.from_orm(user)

    def get_users(self, skip: int = 0, limit: int = 10) -> List[UserSchema]:
        users = self.db.query(UserModel).offset(skip).limit(limit).all()
        return [UserSchema.from_orm(user) for user in users]

    def create_user(self, user_data: UserSchema) -> None:
        hashed_password = user_data.hashed_password()
        user = UserModel(
            id=user_data.id,
            username=user_data.username,
            email=user_data.email,
            avatar_filename=user_data.avatar_filename,
            password_hash=hashed_password,
            role=user_data.role,
            refresh_token=user_data.refresh_token
        )
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        except SQLAlchemyError as e:
            self.db.rollback()
            raise UserError(f"Error creating user: {e}")

    def update_user(self, user_id: int, user_data: UserSchema) -> None:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise UserNotFoundError(user_id)

        # Update fields
        for key, value in user_data.__dict__.items():
            if value is not None:
                setattr(user, key, value)

        if user_data.password:
            user.password_hash = user_data.hashed_password()

        try:
            self.db.commit()
            self.db.refresh(user)
        except SQLAlchemyError as e:
            self.db.rollback()
            raise UserError(f"Error updating user: {e}")

    def delete_user(self, user_id: int) -> None:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise UserNotFoundError(user_id)

        try:
            self.db.delete(user)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise UserError(f"Error deleting user: {e}")

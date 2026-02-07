from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User, Role


class UsersRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, username: str) -> Optional[User]:
        return self.db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_phone(self, phone: str) -> Optional[User]:
        return self.db.query(User).filter(User.phone == phone).first()

    def get_by_identifier(self, identifier: str) -> Optional[User]:
        # ترتیب سلیقه‌ایه، می‌تونی تغییر بدی
        user = self.get_by_username(identifier)
        if user:
            return user
        user = self.get_by_email(identifier)
        if user:
            return user
        return self.get_by_phone(identifier)

    def create_user(self, username: str, email: str | None, phone: str | None, hashed_password: str) -> User:
        user = User(
            username=username,
            email=email,
            phone=phone,
            hashed_password=hashed_password,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def add_role_to_user(self, user: User, role: Role):
        user.roles.append(role)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_role_by_name(self, name: str) -> Optional[Role]:
        return self.db.query(Role).filter(Role.name == name).first()

    def create_role(self, name: str, description: str | None = None) -> Role:
        role = Role(name=name, description=description)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role


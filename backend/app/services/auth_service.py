# app/services/auth_service.py

from typing import Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import secrets
import string

from app.db.session import get_db
from app.repositories.users_repository import UsersRepository
from app.repositories.otp_repository import OTPRepository
from app.schemas.auth import UserCreate
from app.models.otp import OTPPurpose, OTPChannel
from app.core import security
from app.core.config import settings
from app.models.user import User

from jose import JWTError
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login/password")


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.users_repo = UsersRepository(db)
        self.otp_repo = OTPRepository(db)

    # -------- Register --------
    def register_user(self, data: UserCreate) -> User:
        # چک یکتا بودن
        if self.users_repo.get_by_username(data.username):
            raise HTTPException(status_code=400, detail="Username already taken")
        if data.email and self.users_repo.get_by_email(data.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        if data.phone and self.users_repo.get_by_phone(data.phone):
            raise HTTPException(status_code=400, detail="Phone already registered")

        hashed = security.hash_password(data.password)
        user = self.users_repo.create_user(
            username=data.username,
            email=data.email,
            phone=data.phone,
            hashed_password=hashed,
        )
        # اینجا می‌تونی یک role پیش‌فرض مثل "viewer" هم اضافه کنی
        return user

    # -------- Password login --------
    def authenticate_with_password(self, identifier: str, password: str) -> User:
        user = self.users_repo.get_by_identifier(identifier)
        if not user or not security.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User is inactive",
            )
        return user

    def create_token_for_user(self, user: User) -> str:
        roles = [r.name for r in user.roles]
        data = {
            "sub": user.username,
            "user_id": user.id,
            "roles": roles,
        }
        return security.create_access_token(data=data)

    # -------- OTP helpers --------
    def _generate_otp_code(self, length: int = 6) -> str:
        return "".join(secrets.choice(string.digits) for _ in range(length))

    def request_otp(self, target: str, channel: OTPChannel, purpose: OTPPurpose) -> None:
        code = self._generate_otp_code()
        self.otp_repo.create_code(
            target=target,
            channel=channel,
            purpose=purpose,
            code=code,
            ttl_seconds=300,
        )
        # TODO: اینجا واقعی باید SMS / Email بفرستی
        # فعلاً برای dev می‌تونی تو لاگ چاپش کنی
        print(f"[DEV] OTP for {target} ({purpose.value}): {code}")

    def verify_otp_and_login(self, target: str, purpose: OTPPurpose) -> str:
        otp = self.otp_repo.get_latest_valid(target=target, purpose=purpose)
        if not otp:
            raise HTTPException(status_code=400, detail="No valid OTP found")

        # در مرحله‌ی verify route، کد را چک می‌کنیم؛ اینجا فقط توکن می‌سازیم
        user: Optional[User] = None
        # اگر target ایمیل است:
        user = self.users_repo.get_by_email(target)
        if not user:
            # اگر phone است:
            user = self.users_repo.get_by_phone(target)

        if not user:
            raise HTTPException(status_code=404, detail="User not found for this target")

        token = self.create_token_for_user(user)
        self.otp_repo.mark_used(otp)
        return token

    def verify_otp_code(self, target: str, purpose: OTPPurpose, code: str) -> None:
        otp = self.otp_repo.get_latest_valid(target=target, purpose=purpose)
        if not otp or otp.code != code:
            raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    # -------- Forgot / Reset password --------
    def request_password_reset(self, identifier: str) -> None:
        user = self.users_repo.get_by_identifier(identifier)
        if not user:
            # از نظر امنیتی بهتره همیشه success بدی؛ ولی فعلا ساده
            raise HTTPException(status_code=404, detail="User not found")

        target = user.email or user.phone
        if not target:
            raise HTTPException(status_code=400, detail="User has no email/phone")

        channel = OTPChannel.email if user.email else OTPChannel.sms
        self.request_otp(target=target, channel=channel, purpose=OTPPurpose.reset_password)

    def confirm_password_reset(self, identifier: str, code: str, new_password: str) -> None:
        user = self.users_repo.get_by_identifier(identifier)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        target = user.email or user.phone
        if not target:
            raise HTTPException(status_code=400, detail="User has no email/phone")

        self.verify_otp_code(target=target, purpose=OTPPurpose.reset_password, code=code)
        hashed = security.hash_password(new_password)
        user.hashed_password = hashed
        self.db.commit()
        self.db.refresh(user)

    # -------- Current user from token --------
    def get_current_user(self, token: str) -> User:
        try:
            payload = security.decode_token(token)
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        user = self.users_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db=db)


# dependency برای FastAPI
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(get_auth_service),
) -> User:
    return auth_service.get_current_user(token)


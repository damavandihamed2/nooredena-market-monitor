from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth import (
    UserCreate, UserRead, Token,
    LoginWithPassword, OTPRequest, OTPVerify,
    ForgotPasswordRequest, ResetPasswordConfirm,
)
from app.services.auth_service import (
    AuthService, get_auth_service, get_current_user,
)
from app.models.otp import OTPPurpose, OTPChannel
from app.models.user import User

router = APIRouter()


# -------- Register --------
@router.post("/register", response_model=UserRead)
def register(
    data: UserCreate,
    auth_service: AuthService = Depends(get_auth_service),
):
    user = auth_service.register_user(data)
    return user


# -------- Login with password (custom body) --------
@router.post("/login/password", response_model=Token)
def login_with_password(
    data: LoginWithPassword,
    auth_service: AuthService = Depends(get_auth_service),
):
    user = auth_service.authenticate_with_password(
        identifier=data.identifier,
        password=data.password,
    )
    token = auth_service.create_token_for_user(user)
    return Token(access_token=token)


# (اختیاری) پشتیبانی از OAuth2PasswordRequestForm برای /token استاندارد
@router.post("/token", response_model=Token)
def login_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service),
):
    # اینجا username می‌تونه identifier باشه
    user = auth_service.authenticate_with_password(
        identifier=form_data.username,
        password=form_data.password,
    )
    token = auth_service.create_token_for_user(user)
    return Token(access_token=token)


# -------- OTP login --------
@router.post("/login/otp/request")
def request_otp(
    data: OTPRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        channel = OTPChannel(data.channel)
        purpose = OTPPurpose(data.purpose)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid channel or purpose")

    auth_service.request_otp(
        target=data.target,
        channel=channel,
        purpose=purpose,
    )
    return {"detail": "OTP sent"}


@router.post("/login/otp/verify", response_model=Token)
def verify_otp(
    data: OTPVerify,
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        purpose = OTPPurpose(data.purpose)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid purpose")

    auth_service.verify_otp_code(
        target=data.target,
        purpose=purpose,
        code=data.code,
    )

    access_token = auth_service.verify_otp_and_login(
        target=data.target,
        purpose=purpose,
    )
    return Token(access_token=access_token)


# -------- Forgot / Reset password --------
@router.post("/password/forgot")
def forgot_password(
    data: ForgotPasswordRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    auth_service.request_password_reset(identifier=data.identifier)
    return {"detail": "Reset code sent if user exists"}


@router.post("/password/reset")
def reset_password(
    data: ResetPasswordConfirm,
    auth_service: AuthService = Depends(get_auth_service),
):
    auth_service.confirm_password_reset(
        identifier=data.identifier,
        code=data.code,
        new_password=data.new_password,
    )
    return {"detail": "Password has been reset"}


# -------- Me --------
@router.get("/me", response_model=UserRead)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user
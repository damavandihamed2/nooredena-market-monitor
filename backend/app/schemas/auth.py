from typing import List, Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field


class ORMBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


# ---------- User related ----------

class RoleRead(ORMBaseModel):
    id: int
    name: str
    description: Optional[str] = None


class UserBase(ORMBaseModel):
    id: int
    username: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    is_active: bool


class UserRead(UserBase):
    roles: List[RoleRead] = Field(default_factory=lambda: list)


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    password: str = Field(..., min_length=6)


# ---------- Token ----------

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------- Login with password ----------

class LoginWithPassword(BaseModel):
    identifier: str  # username, email or phone
    password: str


# ---------- OTP login ----------

class OTPRequest(BaseModel):
    target: str  # user phone or email address
    channel: str  # "sms" or "email"
    purpose: str = "login"


class OTPVerify(BaseModel):
    target: str
    code: str
    purpose: str = "login"


# ---------- Forgot / Reset password ----------

class ForgotPasswordRequest(BaseModel):
    identifier: str  # username, email or phone


class ResetPasswordConfirm(BaseModel):
    identifier: str
    code: str
    new_password: str = Field(..., min_length=6)
from __future__ import annotations
from datetime import datetime, UTC

from sqlalchemy import (
    Column, Integer, String, Boolean,
    DateTime, Enum
)
import enum

from app.db.base import Base


class OTPPurpose(str, enum.Enum):
    login = "login"
    reset_password = "reset_password"


class OTPChannel(str, enum.Enum):
    sms = "sms"
    email = "email"


class OTPCode(Base):
    __tablename__ = "otp_codes"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True, index=True)

    target = Column(String(255), index=True, nullable=False)   # email or phone
    channel = Column(Enum(OTPChannel), nullable=False)
    purpose = Column(Enum(OTPPurpose), nullable=False)

    code = Column(String(10), nullable=False)  # in professional way it should be hashed
    expires_at = Column(DateTime, nullable=False)
    is_used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(UTC))

    def is_valid(self) -> bool:
        return (not self.is_used) and self.expires_at > datetime.now(UTC)


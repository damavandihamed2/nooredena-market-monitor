from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Session
from app.models.otp import OTPCode, OTPPurpose, OTPChannel


class OTPRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_code(
        self,
        target: str,
        channel: OTPChannel,
        purpose: OTPPurpose,
        code: str,
        ttl_seconds: int = 300,
    ) -> OTPCode:
        expires_at = datetime.utcnow() + timedelta(seconds=ttl_seconds)
        otp = OTPCode(
            target=target,
            channel=channel,
            purpose=purpose,
            code=code,
            expires_at=expires_at,
        )
        self.db.add(otp)
        self.db.commit()
        self.db.refresh(otp)
        return otp

    def get_latest_valid(
        self,
        target: str,
        purpose: OTPPurpose,
    ) -> Optional[OTPCode]:
        return (
            self.db.query(OTPCode)
            .filter(
                OTPCode.target == target,
                OTPCode.purpose == purpose,
                OTPCode.is_used.is_(False),
                OTPCode.expires_at > datetime.utcnow(),
            )
            .order_by(OTPCode.created_at.desc())
            .first()
        )

    def mark_used(self, otp: OTPCode):
        otp.is_used = True
        self.db.commit()
        self.db.refresh(otp)
        return otp


# app/services/market_service.py
from app.repositories.market_repository import MarketRepository

class MarketService:
    def __init__(self, repo: MarketRepository):
        self.repo = repo

    def get_all_symbols(self):
        # اینجا می‌توانی logic اضافه کنی، cache کنی، sort خاص بزنی، ...
        return self.repo.get_all_symbols()

# dependency factory برای FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

def get_market_service(db: Session = Depends(get_db)):
    repo = MarketRepository(db)
    return MarketService(repo)
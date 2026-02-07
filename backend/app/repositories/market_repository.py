# app/repositories/market_repository.py
from sqlalchemy.orm import Session
from app.models.tsetmc import TsetmcSymbols

class MarketRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_symbols(self):
        return self.db.query(TsetmcSymbols).all()

    def get_symbol_by_id(self, symbol_id: int):
        return self.db.query(TsetmcSymbols).filter(TsetmcSymbols.symbol_id == symbol_id).first()

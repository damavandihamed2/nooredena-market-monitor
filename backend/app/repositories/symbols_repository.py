# app/repositories/symbols_repository.py

from sqlalchemy.orm import Session
from app.models.tsetmc import TsetmcSymbols


class SymbolsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, limit: int = 500):
        # مثلاً برای UI لازم نیست کل بازار بیاد
        return (
            self.db.query(TsetmcSymbols)
            .order_by(TsetmcSymbols.symbol)
            .limit(limit)
            .all()
        )

    def get_by_id(self, symbol_id: str):
        return (
            self.db.query(TsetmcSymbols)
            .filter(TsetmcSymbols.symbol_id == symbol_id)
            .first()
        )

    def search_by_name(self, q: str, limit: int = 50):
        pattern = f"%{q}%"
        return (
            self.db.query(TsetmcSymbols)
            .filter(TsetmcSymbols.symbol_name.like(pattern))
            .order_by(TsetmcSymbols.symbol_name)
            .limit(limit)
            .all()
        )
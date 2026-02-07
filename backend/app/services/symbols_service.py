# app/services/symbols_service.py

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.symbols_repository import SymbolsRepository


class SymbolsService:
    def __init__(self, repo: SymbolsRepository):
        self.repo = repo

    def list_symbols(self, limit: int = 500):
        return self.repo.get_all(limit=limit)

    def get_symbol(self, symbol_id: str):
        symbol = self.repo.get_by_id(symbol_id)
        if not symbol:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Symbol not found",
            )
        return symbol

    def search_symbols(self, q: str, limit: int = 50):
        return self.repo.search_by_name(q=q, limit=limit)


# dependency factory برای FastAPI
def get_symbols_service(
    db: Session = Depends(get_db),
) -> SymbolsService:
    repo = SymbolsRepository(db)
    return SymbolsService(repo)
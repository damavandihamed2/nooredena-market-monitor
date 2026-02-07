# app/api/v1/routes_symbols.py

from fastapi import APIRouter, Depends, Query
from typing import List

from app.schemas.symbols import SymbolListItem, SymbolDetail
from app.services.symbols_service import SymbolsService, get_symbols_service

router = APIRouter()


@router.get(
    "/symbols",
    response_model=List[SymbolListItem],
    summary="لیست نمادها",
)
def list_symbols(
    limit: int = Query(500, le=2000),
    service: SymbolsService = Depends(get_symbols_service),
):
    return service.list_symbols(limit=limit)


@router.get(
    "/symbols/{symbol_id}",
    response_model=SymbolDetail,
    summary="جزییات یک نماد",
)
def get_symbol(
    symbol_id: int,
    service: SymbolsService = Depends(get_symbols_service),
):
    return service.get_symbol(symbol_id=symbol_id)


@router.get(
    "/symbols/search/",
    response_model=List[SymbolListItem],
    summary="جست‌وجوی نماد بر اساس نام",
)
def search_symbols(
    q: str = Query(..., min_length=2),
    limit: int = Query(50, le=200),
    service: SymbolsService = Depends(get_symbols_service),
):
    return service.search_symbols(q=q, limit=limit)
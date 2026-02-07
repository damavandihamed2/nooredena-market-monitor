# app/api/v1/routes_market.py
from fastapi import APIRouter, Depends
# from app.schemas.market import SymbolResponse
# from app.services.market_service import MarketService, get_market_service

router = APIRouter()

# @router.get("/symbols", response_model=list[SymbolResponse])
# def list_symbols(service: MarketService = Depends(get_market_service)):
#     return service.get_all_symbols()


# app/schemas/market.py
from pydantic import BaseModel, ConfigDict


class SymbolBase(BaseModel):
    symbol: str
    name: str


class SymbolResponse(SymbolBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


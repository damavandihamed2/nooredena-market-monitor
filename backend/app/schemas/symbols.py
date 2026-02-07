# app/schemas/symbols.py

from pydantic import BaseModel, ConfigDict

class SymbolBase(BaseModel):
    symbol_id: str
    symbol: str
    symbol_name: str | None = None
    symbol_name_eng: str | None = None
    symbol_eng: str | None = None


class SymbolListItem(SymbolBase):
    """برای نمایش در لیست نمادها"""
    pass


class SymbolDetail(SymbolBase):

    """اگر بعداً خواستی جزییات بیشتری بدهی، اینجا اضافه می‌کنی."""
    # مثلا:
    # category: str | None = None
    # status_name: str | None = None
    model_config = ConfigDict(from_attributes=True)
    pass


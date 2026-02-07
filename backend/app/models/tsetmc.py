from __future__ import annotations

from typing import Optional
from sqlalchemy import Column, BigInteger, Float, Integer, SmallInteger, String, Text, PrimaryKeyConstraint
from app.models.base import Base


class TsetmcSymbols(Base):
    __tablename__ = "symbols"
    __table_args__ = (
        PrimaryKeyConstraint(
            "symbol_id",
        ),
        {"schema": "tsetmc"}
    )

    symbol: Optional[str] = Column(String(50), nullable=True)
    symbol_name: Optional[str] = Column(String(255), nullable=True)
    symbol_name_eng: Optional[str] = Column(String(50), nullable=True)
    symbol_id: Optional[str] = Column(String(50), nullable=True)
    symbol_id_2: Optional[str] = Column(String(50), nullable=True)
    symbol_id_3: Optional[str] = Column(String(50), nullable=True)
    symbol_id_4: Optional[str] = Column(String(50), nullable=True)
    symbol_eng: Optional[str] = Column(String(50), nullable=True)
    symbol_code: Optional[str] = Column(String(50), nullable=True)
    company: Optional[str] = Column(String(50), nullable=True)
    company_code: Optional[str] = Column(String(50), nullable=True)
    sector: Optional[str] = Column(String(50), nullable=True)
    sector_name: Optional[str] = Column(String(255), nullable=True)
    subsector: Optional[str] = Column(String(50), nullable=True)
    subsector_name: Optional[str] = Column(String(255), nullable=True)
    flow: Optional[int] = Column(SmallInteger, nullable=True)
    flow_name: Optional[str] = Column(String(50), nullable=True)
    yval: Optional[str] = Column(String(50), nullable=True)
    description: Optional[str] = Column(Text, nullable=True)
    total_share: Optional[int] = Column(BigInteger, nullable=True)
    floating_share: Optional[int] = Column(Integer, nullable=True)
    base_volume: Optional[int] = Column(BigInteger, nullable=True)
    monthly_mean_volume: Optional[int] = Column(BigInteger, nullable=True)
    top_symbol: Optional[int] = Column(SmallInteger, nullable=True)
    estimated_eps: Optional[int] = Column(BigInteger, nullable=True)
    psr: Optional[float] = Column(Float, nullable=True)
    sector_pe: Optional[float] = Column(Float, nullable=True)
    nav: Optional[int] = Column(Integer, nullable=True)
    min_week: Optional[int] = Column(Integer, nullable=True)
    max_week: Optional[int] = Column(Integer, nullable=True)
    min_year: Optional[int] = Column(Integer, nullable=True)
    max_year: Optional[int] = Column(Integer, nullable=True)
    open_price: Optional[int] = Column(Integer, nullable=True)
    high_price: Optional[int] = Column(Integer, nullable=True)
    low_price: Optional[int] = Column(Integer, nullable=True)
    close_price: Optional[int] = Column(Integer, nullable=True)
    final_price: Optional[int] = Column(Integer, nullable=True)
    yesterday_price: Optional[int] = Column(Integer, nullable=True)
    change_price: Optional[int] = Column(Integer, nullable=True)
    trade_amount: Optional[int] = Column(Integer, nullable=True)
    trade_volume: Optional[int] = Column(BigInteger, nullable=True)
    trade_value: Optional[int] = Column(BigInteger, nullable=True)
    under_supervision: Optional[int] = Column(SmallInteger, nullable=True)
    status: Optional[str] = Column(String(50), nullable=True)
    status_name: Optional[str] = Column(String(50), nullable=True)
    board: Optional[int] = Column(SmallInteger, nullable=True)
    sttc_thr_max: Optional[int] = Column(Integer, nullable=True)
    sttc_thr_min: Optional[int] = Column(Integer, nullable=True)
    last_date: Optional[int] = Column(Integer, nullable=True)
    last_time: Optional[int] = Column(Integer, nullable=True)
    final_last_date: Optional[int] = Column(Integer, nullable=True)
    category: Optional[str] = Column(String(50), nullable=True)
    category_name: Optional[str] = Column(String(255), nullable=True)
    last: Optional[str] = Column(String(50), nullable=True)
    iclose: Optional[str] = Column(String(50), nullable=True)
    yclose: Optional[str] = Column(String(50), nullable=True)
    date: Optional[str] = Column("date_", String(10), nullable=True)
    time: Optional[str] = Column("time_", String(10), nullable=True)
    active: Optional[int] = Column(SmallInteger, nullable=True)
    fund_units_issued: Optional[int] = Column(BigInteger, nullable=True)
    fund_units_date: Optional[int] = Column(Integer, nullable=True)


class TsetmcSymbolsClienttype(Base):
    __tablename__ = "symbols_clienttype"
    __table_args__ = (
        PrimaryKeyConstraint(
            "symbol_id",
            "date",
        ),
        {"schema": "tsetmc"}
    )

    symbol_id: Optional[str] = Column(String(50), nullable=True)
    date: Optional[int] = Column(Integer, nullable=True)
    buy_i_count: Optional[int] = Column(Integer, nullable=True)
    buy_i_volume: Optional[int] = Column(BigInteger, nullable=True)
    buy_i_value: Optional[int] = Column(BigInteger, nullable=True)
    buy_n_count: Optional[int] = Column(Integer, nullable=True)
    buy_n_volume: Optional[int] = Column(BigInteger, nullable=True)
    buy_n_value: Optional[int] = Column(BigInteger, nullable=True)
    sell_i_count: Optional[int] = Column(Integer, nullable=True)
    sell_i_volume: Optional[int] = Column(BigInteger, nullable=True)
    sell_i_value: Optional[int] = Column(BigInteger, nullable=True)
    sell_n_count: Optional[int] = Column(Integer, nullable=True)
    sell_n_volume: Optional[int] = Column(BigInteger, nullable=True)
    sell_n_value: Optional[int] = Column(BigInteger, nullable=True)

class TsetmcSymbolsHistory(Base):
    __tablename__ = "symbols_history"
    __table_args__ = (
        PrimaryKeyConstraint(
            "symbol_id",
            "date",
        ),
        {"schema": "tsetmc"}
    )

    date: Optional[int] = Column(Integer, nullable=True)
    symbol_id: Optional[str] = Column(String(50), nullable=True)
    open_price: Optional[int] = Column(Integer, nullable=True)
    high_price: Optional[int] = Column(Integer, nullable=True)
    low_price: Optional[int] = Column(Integer, nullable=True)
    close_price: Optional[int] = Column(Integer, nullable=True)
    yesterday_price: Optional[int] = Column(Integer, nullable=True)
    final_price: Optional[int] = Column(Integer, nullable=True)
    trade_amount: Optional[int] = Column(BigInteger, nullable=True)
    trade_volume: Optional[int] = Column(BigInteger, nullable=True)
    trade_value: Optional[int] = Column(BigInteger, nullable=True)


class TsetmcSymbolsRos(Base):
    __tablename__ = "symbols_ros"
    __table_args__ = (
        PrimaryKeyConstraint(
            "symbol_id",
        ),
        {"schema": "tsetmc"}
    )

    symbol_ros: Optional[str] = Column(String(50), nullable=True)
    symbol_id: Optional[str] = Column(String(50), nullable=True)
    symbol_id_2: Optional[str] = Column(String(50), nullable=True)
    symbol_id_3: Optional[str] = Column(String(50), nullable=True)
    symbol_id_4: Optional[str] = Column(String(50), nullable=True)
    active: Optional[int] = Column(Integer, nullable=True)
    symbol: Optional[str] = Column(String(50), nullable=True)
    date: Optional[str] = Column("date_", String(50), nullable=True)
    time: Optional[str] = Column("time_", String(50), nullable=True)


class TsetmcSymbolsRosClienttype(Base):
    __tablename__ = "symbols_ros_clienttype"
    __table_args__ = (
        PrimaryKeyConstraint(
            "symbol_id",
            "date",
        ),
        {"schema": "tsetmc"}
    )

    symbol_id: Optional[str] = Column(String(50), nullable=True)
    date: Optional[int] = Column(Integer, nullable=True)
    buy_i_count: Optional[int] = Column(Integer, nullable=True)
    buy_i_volume: Optional[int] = Column(BigInteger, nullable=True)
    buy_i_value: Optional[int] = Column(BigInteger, nullable=True)
    buy_n_count: Optional[int] = Column(Integer, nullable=True)
    buy_n_volume: Optional[int] = Column(BigInteger, nullable=True)
    buy_n_value: Optional[int] = Column(BigInteger, nullable=True)
    sell_i_count: Optional[int] = Column(Integer, nullable=True)
    sell_i_volume: Optional[int] = Column(BigInteger, nullable=True)
    sell_i_value: Optional[int] = Column(BigInteger, nullable=True)
    sell_n_count: Optional[int] = Column(Integer, nullable=True)
    sell_n_volume: Optional[int] = Column(BigInteger, nullable=True)
    sell_n_value: Optional[int] = Column(BigInteger, nullable=True)


class TsetmcSymbolsRosHistory(Base):
    __tablename__ = "symbols_ros_history"
    __table_args__ = (
        PrimaryKeyConstraint(
            "symbol_id",
            "date",
        ),
        {"schema": "tsetmc"}
    )

    date: Optional[int] = Column(Integer, nullable=True)
    symbol_id: Optional[str] = Column(String(50), nullable=True)
    open_price: Optional[int] = Column(Integer, nullable=True)
    high_price: Optional[int] = Column(Integer, nullable=True)
    low_price: Optional[int] = Column(Integer, nullable=True)
    close_price: Optional[int] = Column(Integer, nullable=True)
    yesterday_price: Optional[int] = Column(Integer, nullable=True)
    final_price: Optional[int] = Column(Integer, nullable=True)
    trade_amount: Optional[int] = Column(BigInteger, nullable=True)
    trade_volume: Optional[int] = Column(BigInteger, nullable=True)
    trade_value: Optional[int] = Column(BigInteger, nullable=True)


class TsetmcSymbolsDataToday(Base):
    __tablename__ = "symbols_data_today"
    __table_args__ = (
        PrimaryKeyConstraint(
            "symbol_id",
        ),
        {"schema": "tsetmc"}
    )

    symbol_id: Optional[str] = Column(String(50), nullable=True)
    symbol_name_eng: Optional[str] = Column(String(50), nullable=True)
    symbol: Optional[str] = Column(String(50), nullable=True)
    symbol_name: Optional[str] = Column(String(255), nullable=True)
    heven: Optional[int] = Column(Integer, nullable=True)
    first_price: Optional[int] = Column(Integer, nullable=True)
    close_price: Optional[int] = Column(Integer, nullable=True)
    last_price: Optional[int] = Column(Integer, nullable=True)
    trade_number: Optional[int] = Column(BigInteger, nullable=True)
    trade_volume: Optional[int] = Column(BigInteger, nullable=True)
    trade_value: Optional[int] = Column(BigInteger, nullable=True)
    day_low: Optional[int] = Column(Integer, nullable=True)
    day_high: Optional[int] = Column(Integer, nullable=True)
    yesterday_price: Optional[int] = Column(Integer, nullable=True)
    eps: Optional[int] = Column(Integer, nullable=True)
    base_volume: Optional[int] = Column(BigInteger, nullable=True)
    visit_count: Optional[int] = Column(Integer, nullable=True)
    flow: Optional[int] = Column(Integer, nullable=True)
    sector: Optional[str] = Column(String(255), nullable=True)
    day_max: Optional[int] = Column(BigInteger, nullable=True)
    day_min: Optional[int] = Column(Integer, nullable=True)
    share_number: Optional[int] = Column(BigInteger, nullable=True)
    yval: Optional[int] = Column(Integer, nullable=True)
    nav: Optional[int] = Column(BigInteger, nullable=True)
    open_position: Optional[int] = Column(BigInteger, nullable=True)
    close_change: Optional[float] = Column(Float, nullable=True)
    last_change: Optional[float] = Column(Float, nullable=True)
    sell_count: Optional[int] = Column(Integer, nullable=True)
    buy_count: Optional[int] = Column(Integer, nullable=True)
    buy_price: Optional[int] = Column(Integer, nullable=True)
    sell_price: Optional[int] = Column(Integer, nullable=True)
    buy_volume: Optional[int] = Column(BigInteger, nullable=True)
    sell_volume: Optional[int] = Column(BigInteger, nullable=True)
    buy_number_natural: Optional[int] = Column(Integer, nullable=True)
    buy_number_legal: Optional[int] = Column(Integer, nullable=True)
    buy_volume_natural: Optional[int] = Column(BigInteger, nullable=True)
    buy_volume_legal: Optional[int] = Column(BigInteger, nullable=True)
    sell_number_natural: Optional[int] = Column(Integer, nullable=True)
    sell_number_legal: Optional[int] = Column(Integer, nullable=True)
    sell_volume_natural: Optional[int] = Column(BigInteger, nullable=True)
    sell_volume_legal: Optional[int] = Column(BigInteger, nullable=True)
    money_in_out_natural: Optional[int] = Column(BigInteger, nullable=True)
    mean_buy_natural: Optional[int] = Column(BigInteger, nullable=True)
    mean_sell_natural: Optional[int] = Column(BigInteger, nullable=True)
    buyer_to_seller_power: Optional[float] = Column(Float, nullable=True)
    block: Optional[int] = Column(SmallInteger, nullable=True)
    date: Optional[str] = Column(String(255), nullable=True)
    time: Optional[str] = Column(String(255), nullable=True)
    category: Optional[str] = Column(String(10), nullable=True)


class TsetmcSymbolsDividend(Base):
    __tablename__ = "symbols_dividend"
    __table_args__ = (
        PrimaryKeyConstraint(
            "symbol_id",
            "date"
        ),
        {"schema": "tsetmc"}
    )

    symbol_id: Optional[str] = Column(String(50), nullable=True)
    date: Optional[int] = Column(Integer, nullable=True)
    price_old: Optional[int] = Column(Integer, nullable=True)
    price_new: Optional[int] = Column(Integer, nullable=True)
    is_adjusted: Optional[int] = Column(Integer, nullable=True)


class TsetmcIndices(Base):
    __tablename__ = "indices"
    __table_args__ = (
        PrimaryKeyConstraint(
            "indices",
        ),
        {"schema": "tsetmc"}
    )

    indices: Optional[str] = Column(String(50), nullable=True)
    indices_name: Optional[str] = Column(String(255), nullable=True)
    indices_id: Optional[str] = Column(String(50), nullable=True)


class TsetmcIndicesHistory(Base):
    __tablename__ = "indices_history"
    __table_args__ = (
        PrimaryKeyConstraint(
            "indices_id",
            "date"
        ),
        {"schema": "tsetmc"}
    )

    indices_id: Optional[str] = Column(String(50), nullable=True)
    date: Optional[int] = Column(Integer, nullable=True)
    close_price: Optional[float] = Column(Float, nullable=True)
    low_price: Optional[float] = Column(Float, nullable=True)
    high_price: Optional[float] = Column(Float, nullable=True)


class TsetmcMarketDataToday(Base):
    __tablename__ = "market_data_today"
    __table_args__ = (
        PrimaryKeyConstraint(
            "date",
            "time"
        ),
        {"schema": "tsetmc"}
    )

    total_index: Optional[float] = Column(Float, nullable=True)
    total_index_equal: Optional[float] = Column(Float, nullable=True)
    market_value: Optional[int] = Column(BigInteger, nullable=True)
    trade_amount: Optional[int] = Column(Integer, nullable=True)
    trade_value: Optional[int] = Column(BigInteger, nullable=True)
    trade_volume: Optional[int] = Column(BigInteger, nullable=True)
    total_index_change: Optional[int] = Column(Integer, nullable=True)
    total_index_equal_change: Optional[int] = Column(Integer, nullable=True)
    market_state: Optional[str] = Column(String(50), nullable=True)
    market_state_title: Optional[str] = Column(String(50), nullable=True)
    market_activity_date: Optional[str] = Column(String(50), nullable=True)
    market_activity_time: Optional[str] = Column(String(50), nullable=True)
    date: Optional[str] = Column(String(255), nullable=True)
    time: Optional[str] = Column(String(255), nullable=True)


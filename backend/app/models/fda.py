from __future__ import annotations

from typing import Optional
from sqlalchemy import Column, BigInteger, Float, Integer, String, Text, PrimaryKeyConstraint
from .base import Base


class FdaATCs(Base):
    __tablename__ = "ATCs"
    __table_args__ = (
        PrimaryKeyConstraint(
            "ATC_id"
        ),
        {"schema": "fda"}
    )

    ATC_id: Optional[int] = Column(Integer, nullable=True)
    ATC: Optional[str] = Column(String(50), nullable=True)
    ATC_1: Optional[str] = Column(Text, nullable=True)
    ATC_2: Optional[str] = Column(Text, nullable=True)
    ATC_3: Optional[str] = Column(Text, nullable=True)
    ATC_4: Optional[str] = Column(Text, nullable=True)
    ATC_5: Optional[str] = Column(Text, nullable=True)


class FdaROAs(Base):
    __tablename__ = "ROAs"
    __table_args__ = (
        PrimaryKeyConstraint(
            "roa_id"
        ),
        {"schema": "fda"}
    )

    roa_id: Optional[int] = Column(Integer, nullable=True)
    roa: Optional[str] = Column(String(50), nullable=True)


class FdaBrandOwners(Base):
    __tablename__ = "brand_owners"
    __table_args__ = (
        PrimaryKeyConstraint(
            "brand_owner_id"
        ),
        {"schema": "fda"}
    )

    brand_owner_id: Optional[int] = Column(Integer, nullable=True)
    brand_owner: Optional[str] = Column(Text, nullable=True)


class FdaDosageForms(Base):
    __tablename__ = "dosage_forms"
    __table_args__ = (
        PrimaryKeyConstraint(
            "dosage_form_id"
        ),
        {"schema": "fda"}
    )

    dosage_form_id: Optional[int] = Column(Integer, nullable=True)
    dosage_form: Optional[str] = Column(Text, nullable=True)


class FdaLicenseOwners(Base):
    __tablename__ = "license_owners"
    __table_args__ = (
        PrimaryKeyConstraint(
            "license_owner_id"
        ),
        {"schema": "fda"}
    )

    license_owner_id: Optional[int] = Column(Integer, nullable=True)
    license_owner: Optional[str] = Column(Text, nullable=True)


class FdaMedicines(Base):
    __tablename__ = "medicines"
    __table_args__ = (
        PrimaryKeyConstraint(
            "medicine_id"
        ),
        {"schema": "fda"}
    )

    date: Optional[str] = Column(String(10), nullable=True)
    medicine_id: Optional[int] = Column(Integer, nullable=True)
    link: Optional[str] = Column(String(64), nullable=True)
    name_persian: Optional[str] = Column(String(1024), nullable=True)
    generic_code: Optional[int] = Column(Integer, nullable=True)
    name: Optional[str] = Column(String(512), nullable=True)
    general_name: Optional[str] = Column(String(1024), nullable=True)
    license_date: Optional[str] = Column(String(10), nullable=True)
    package: Optional[str] = Column(String(512), nullable=True)
    GTIN: Optional[str] = Column(String(32), nullable=True)
    IRC: Optional[str] = Column(String(32), nullable=True)
    dosage_form_id: Optional[int] = Column(Integer, nullable=True)
    roa_id: Optional[int] = Column(Integer, nullable=True)
    brand_owner_id: Optional[int] = Column(Integer, nullable=True)
    license_owner_id: Optional[int] = Column(Integer, nullable=True)
    producer_id: Optional[int] = Column(Integer, nullable=True)
    ATC_id: Optional[int] = Column(Integer, nullable=True)
    consumer_package_price: Optional[int] = Column(BigInteger, nullable=True)
    price: Optional[int] = Column(BigInteger, nullable=True)


class FdaMedicinesAtcSearch(Base):
    __tablename__ = "medicines_atc_search"
    __table_args__ = (
        PrimaryKeyConstraint(
            "medicine_id"
        ),
        {"schema": "fda"}
    )

    date: Optional[str] = Column(String(10), nullable=True)
    medicine_id: Optional[int] = Column(Integer, nullable=True)
    link: Optional[str] = Column(String(64), nullable=True)
    name_persian: Optional[str] = Column(String(1024), nullable=True)
    name_latin: Optional[str] = Column(String(1024), nullable=True)
    brand_owner_id: Optional[int] = Column(Integer, nullable=True)
    license_owner_id: Optional[int] = Column(Integer, nullable=True)
    package: Optional[str] = Column(String(512), nullable=True)
    product_code: Optional[str] = Column(String(32), nullable=True)
    generic_code: Optional[int] = Column(Integer, nullable=True)


class FdaMedicinesHistory(Base):
    __tablename__ = "medicines_history"
    __table_args__ = (
        PrimaryKeyConstraint(
            "medicine_id",
            "date"
        ),
        {"schema": "fda"}
    )

    date: Optional[str] = Column(String(50), nullable=True)
    medicine_id: Optional[int] = Column(Integer, nullable=True)
    consumer_package_price: Optional[int] = Column(BigInteger, nullable=True)
    price: Optional[int] = Column(BigInteger, nullable=True)


class FdaMedicinesHistorySelected(Base):
    __tablename__ = "medicines_history_selected"
    __table_args__ = (
        PrimaryKeyConstraint(
            "medicine_id",
            "date"
        ),
        {"schema": "fda"}
    )

    date: Optional[str] = Column(String(50), nullable=True)
    medicine_id: Optional[int] = Column(Integer, nullable=True)
    consumer_package_price: Optional[int] = Column(BigInteger, nullable=True)
    price: Optional[int] = Column(BigInteger, nullable=True)


class FdaMedicinesPage(Base):
    __tablename__ = "medicines_page"
    __table_args__ = (
        PrimaryKeyConstraint(
            "medicine_id"
        ),
        {"schema": "fda"}
    )

    date: Optional[str] = Column(String(10), nullable=True)
    medicine_id: Optional[int] = Column(Integer, nullable=True)
    link: Optional[str] = Column(String(64), nullable=True)
    name: Optional[str] = Column(String(512), nullable=True)
    dosage_form_id: Optional[int] = Column(Integer, nullable=True)
    roa_id: Optional[int] = Column(Integer, nullable=True)
    license_owner_id: Optional[int] = Column(Integer, nullable=True)
    brand_owner_id: Optional[int] = Column(Integer, nullable=True)
    producer_id: Optional[int] = Column(Integer, nullable=True)
    license_date: Optional[str] = Column(String(10), nullable=True)
    consumer_package_price: Optional[int] = Column(BigInteger, nullable=True)
    GTIN: Optional[str] = Column(String(32), nullable=True)
    IRC: Optional[str] = Column(String(32), nullable=True)
    package: Optional[str] = Column(String(512), nullable=True)
    general_name: Optional[str] = Column(String(1024), nullable=True)
    price: Optional[int] = Column(BigInteger, nullable=True)
    ATC_id: Optional[int] = Column(Integer, nullable=True)


class FdaMedicinesWeight(Base):
    __tablename__ = "medicines_weight"
    __table_args__ = (
        PrimaryKeyConstraint(
            "link",
            "date"
        ),
        {"schema": "fda"}
    )

    date: Optional[str] = Column(String(50), nullable=True)
    link: Optional[str] = Column(String(50), nullable=True)
    symbol: Optional[str] = Column(String(50), nullable=True)
    general_name: Optional[str] = Column(String(255), nullable=True)
    weight: Optional[float] = Column(Float, nullable=True)
    quantity: Optional[int] = Column(BigInteger, nullable=True)


class FdaProducers(Base):
    __tablename__ = "producers"
    __table_args__ = (
        PrimaryKeyConstraint(
            "producer_id"
        ),
        {"schema": "fda"}
    )

    producer_id: Optional[int] = Column(Integer, nullable=True)
    producer: Optional[str] = Column(Text, nullable=True)

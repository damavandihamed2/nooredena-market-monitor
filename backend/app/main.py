# app/main.py
from fastapi import FastAPI
from app.api.v1 import routes_symbols, routes_auth
# from app.api.v1 import routes_market, routes_portfolio, routes_auth

app = FastAPI(title="Nooredena Market Monitor API", version="1.0.0")


# registering routers

app.include_router(routes_symbols.router, prefix="/api/v1", tags=["symbols"])
app.include_router(routes_auth.router, prefix="/api/v1/auth", tags=["auth"])
# app.include_router(routes_market.router, prefix="/api/v1/market", tags=["market"])
# app.include_router(routes_portfolio.router, prefix="/api/v1/portfolio", tags=["portfolio"])
# app.include_router(routes_auth.router, prefix="/api/v1/auth", tags=["auth"])
# app/main.py





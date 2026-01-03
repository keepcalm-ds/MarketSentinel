from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="MarketSentinel")

app.include_router(router)

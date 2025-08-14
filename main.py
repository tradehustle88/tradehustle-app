from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

APP = FastAPI(title="TradeHustle API", version="1.0.0")

APP.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@APP.get("/api/health")
async def health():
    return {"ok": True, "service": "TradeHustle API", "version": APP.version}

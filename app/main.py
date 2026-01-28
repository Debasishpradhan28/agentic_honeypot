from fastapi import FastAPI
from app.routes.message import router

app = FastAPI(title="Agentic Honey-Pot API")

app.include_router(router, prefix="/api")

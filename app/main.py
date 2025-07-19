from fastapi import FastAPI
from app.routes import donate, history

app = FastAPI()

app.include_router(donate.router)
app.include_router(history.router)

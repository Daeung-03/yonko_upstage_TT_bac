from fastapi import FastAPI
from app.routers import terms, chat, calendar, notifications

app = FastAPI(title="Term Tracker API", version="0.1.0")

app.include_router(terms.router,         prefix="/terms",         tags=["Terms"])
app.include_router(chat.router,          prefix="/chat",          tags=["Chat"])
app.include_router(calendar.router,      prefix="/calendar",      tags=["Calendar"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}
from app.config import settings
print("📌 DATABASE_URL:", settings.DATABASE_URL)

import asyncio

from sqlalchemy import text
from app.database import engine
from app.models import *  # 모든 모델 import (테이블 인식용)
from app.database import Base

async def test_connection():
    # 1. 연결 확인
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("✅ DB 연결 성공:", result.scalar())

async def create_tables():
    # 2. 테이블 생성 (최초 1회)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 테이블 생성 완료")

async def main():
    await test_connection()
    await create_tables()

asyncio.run(main())
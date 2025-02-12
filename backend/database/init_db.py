from backend.models.shorthand_model import Base
from sqlalchemy.ext.asyncio import create_async_engine

DB_PATH="sqlite+aiosqlite:///./test.db"

async def make_db():
    engine = create_async_engine(DB_PATH, echo=True)

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

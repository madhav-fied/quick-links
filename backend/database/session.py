from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker


DB_PATH="sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DB_PATH)

AsyncEngine = async_sessionmaker(engine)

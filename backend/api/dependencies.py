from backend.database.session import AsyncEngine

async def get_db():
    async with AsyncEngine() as session:
        try:
            yield session
        finally:
            await session.close()

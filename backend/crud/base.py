from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession


class CrudBase:
    def __init__(self, model):
        self.model = model
    
    async def create_record(self, db: AsyncSession, obj):
        entry = self.model(**obj.model_dump())
        db.add(entry)
        await db.commit()
        return entry
    
    async def delete_record(self, db: AsyncSession, **kwargs):
        query_model = delete(self.model).filter_by(**kwargs)
        await db.execute(query_model)
        await db.commit()
    
    async def get_all(self, db):
        query_model = select(self.model)
        exe = await db.execute(query_model)
        rows = exe.scalars().fetchall()
        return rows

from backend.crud.base import CrudBase
from backend.models.shorthand_model import URLShorthand
from sqlalchemy import select

class QuickRedirectCRUD(CrudBase):
    def __init__(self):
        super().__init__(model=URLShorthand)
    
    async def get_url_by_shorthand(self, db, shorthand):
        query_model = select(self.model.url).filter(self.model.shorthand == shorthand)
        executed = await db.execute(query_model)
        return executed.scalars().first()    


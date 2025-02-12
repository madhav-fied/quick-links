from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from backend.schemas.redirect import URLShorthand
from backend.api.dependencies import get_db
from backend.crud.quick_redirect_crud import QuickRedirectCRUD
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/go/{shorthand}", response_class=RedirectResponse, status_code=302)
async def get_url_for_shorthand(shorthand: str, db: AsyncSession = Depends(get_db)):
    crud = QuickRedirectCRUD()
    data = await crud.get_url_by_shorthand(db=db, shorthand=shorthand)
    return data

@router.post("/add")
async def insert_record(data: URLShorthand, db: AsyncSession = Depends(get_db)):
    crud = QuickRedirectCRUD()
    await crud.create_record(db=db, obj=data)
    return "OK"
    try:
        await crud.create_record(db=db, obj=data)
        return "OK"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        

@router.get("/view")
async def get_list(db: AsyncSession = Depends(get_db)):
    crud = QuickRedirectCRUD()
    data = await crud.get_all(db=db)
    return data

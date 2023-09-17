from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.ext.asyncio import AsyncSession
from src.controllers.products.product_schema import ProductCreate
from src.db import get_session
from src.controllers.products import product_service
router = APIRouter()

@router.post("/product")
async def create(
    data: ProductCreate,
    db: AsyncSession= Depends(get_session),
    auth: AuthJWT = Depends()
):
    
    product_id = await product_service.create_product(db, data)
    product = await product_service.get_product(db, product_id)
    return product.to_json
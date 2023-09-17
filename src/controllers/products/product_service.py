from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.product import Product

from src.controllers.products.product_schema import ProductCreate

async def create_product(db: AsyncSession, data: ProductCreate):
    shop_id = data.shop_id
    price = data.price
    description = data.description
    name = data.name
    img_url = data.img_url

    stm = insert(Product).values(shop_id = shop_id, price = price, description= description, name=name, img_url= img_url)

    product = await db.execute(stm)
    await db.commit()
    return product.lastrowid

async def get_product(db:AsyncSession, id: int):
    stm = select(Product).filter_by(id = id)
    product = (await db.execute(stm)).scalars().first()
    return product
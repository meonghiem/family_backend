from datetime import timedelta
import json
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import or_, select, insert
from fastapi_jwt_auth import AuthJWT
from src.models.account import Shop
from src.models import Customer
from src.controllers.auth.auth_schema import SignUpRequest
async def check_account(db: AsyncSession, username:str, password: str):
    stm = select(Customer).filter_by(username = username, password = password)
    customer = (await db.execute(stm)).scalars().first()
    return customer

async def check_shop(db:AsyncSession, id: int):
    stm = select(Shop).filter_by(id=id)
    shop = (await db.execute(stm)).scalars().first()
    return shop
    
async def create_customer(db: AsyncSession, data: SignUpRequest):
    stm = select(Customer).filter(or_(

        Customer.username== data.username,
        Customer.email == data.email
    )
        )
    customer = (await db.execute(stm)).scalars().first()
    if customer:
        raise HTTPException(detail='username or email has already existed', status_code=400)
    stm = insert(Customer).values(
        username= data.username,
        password= data.password,
        phone= data.phone,
        email= data.email,
        address= data.address,
    )
    
    res = await db.execute(stm)
    await db.commit()
    return res.lastrowid

async def get_customer(db:AsyncSession, id: int):
    stm = select(Customer).filter(Customer.id==id)
    customer = (await db.execute(stm)).scalars().first()
    return customer

async def create_token(auth: AuthJWT, obj):
    subject = json.dumps(obj)
    access_token = auth.create_access_token(subject= subject,algorithm="HS256", expires_time=timedelta(hours = 4))
    refresh_token = auth.create_access_token(subject= subject,algorithm="HS256", expires_time=timedelta(days = 4))
    obj["access_token"] = access_token
    obj["refresh_token"] = refresh_token
    return obj
    
    
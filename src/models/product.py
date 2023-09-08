from sqlalchemy import Column, Integer, String, DateTime, func, Double, ForeignKey   
from .base import BaseModel

class Product(BaseModel):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, )
    name= Column(String(255), nullable=False)
    price = Column(Double, nullable=False)
    img_url=Column(String(255))
    shop_id = Column(Integer, ForeignKey("shop.id", ondelete="CASCADE"), nullable=False)
    description = Column(String(255))
    updated_at = Column(DateTime, server_onupdate=func.now())
    created_at = Column(DateTime, server_default=func.now())
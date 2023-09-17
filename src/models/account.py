
from sqlalchemy import Column, Integer, String, DateTime, func, Double, ForeignKey, DDL
from typing import List
from .base import BaseModel
from sqlalchemy.orm import relationship,Mapped

class Customer(BaseModel):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True )
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    # role_id = Column(Integer, default=1) # 1: user, 2: shop, 3: admin
    phone = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True, unique=True)
    address = Column(String(255), nullable=True)
    invoices:Mapped[List["Invoice"]] = relationship( back_populates="customer", lazy='dynamic')
    
    @property
    def to_json(self):
        return {
            "id": self.id,
            "username":self.username,
            "created_at": str(self.created_at),
            "phone": self.phone,
            "address": self.address
        }
    
# class Customer(Account):
#     __tablename__ = 'customer'
#     id = Column(Integer, ForeignKey('account.id'), primary_key=True)
#     invoices:Mapped[List["Invoice"]] = relationship( back_populates="customer", lazy='dynamic')
#     __mapper_args__ = {
#         'polymorphic_identity': 'customer'
#     }
#     pass
class Shop(BaseModel):
    __tablename__ = 'shop'
    id = Column(Integer, ForeignKey('customer.id'), primary_key=True)
    invoices:Mapped[List["Invoice"]] = relationship( back_populates="shop", lazy='dynamic')
    info = relationship('Customer', foreign_keys=[id], innerjoin=True)
    
class Admin(BaseModel):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pass
    

# # trigger DDL
# trigger = DDL('''\
#     CREATE TRIGGER create_record AFTER INSERT 
#     ''')
    
    
    
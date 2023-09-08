from sqlalchemy import Column, Integer, String, DateTime, func, Double, ForeignKey ,Boolean, CheckConstraint
from .base import BaseModel
from sqlalchemy.orm import relationship, Mapped

class Invoice(BaseModel):
    __tablename__ = 'invoice'
    id = Column(Integer,primary_key=True )
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    shop_id = Column(Integer, ForeignKey("shop.id"), nullable=False)
    is_export = Column(Boolean, nullable=False, default=1)
    total_amount = Column(Double, nullable=False)
    is_paid = Column(Boolean, nullable=False, default=0)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())
    invoice_details = relationship('InvoiceDetail',back_populates="invoice")
    shop = relationship('Shop',back_populates="invoices")
    customer = relationship('Customer',back_populates="invoices")
    
    
class InvoiceDetail(BaseModel):
    __tablename__ = 'invoice_detail'
    id = Column(Integer,primary_key=True, )
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"),nullable=False)
    invoice_id = Column(Integer, ForeignKey("invoice.id", ondelete="CASCADE"),nullable=False)
    quantity = Column(Integer, nullable=False)
    invoice = relationship('Invoice', back_populates="invoice_details")
    
    
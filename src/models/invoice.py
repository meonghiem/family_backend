from sqlalchemy import Column, Integer, String, DateTime, func, Double, ForeignKey ,Boolean, CheckConstraint
from .base import BaseModel
from sqlalchemy.orm import relationship, Mapped

class Invoice(BaseModel):
    __tablename__ = 'invoice'
    id = Column(Integer,primary_key=True )
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    shop_id = Column(Integer, ForeignKey("shop.id"), nullable=False)
    is_export = Column(Boolean, nullable=False, server_default="1") # da xuat hang chua
    total_amount = Column(Double, nullable=False, server_default="0")
    is_paid = Column(Boolean, nullable=False, server_default="0") # da tra tien chua
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())
    invoice_details = relationship('InvoiceDetail',back_populates="invoice")
    shop = relationship('Shop',back_populates="invoices")
    customer = relationship('Customer',back_populates="invoices")
    type = Column(Integer, server_default="0") # 0: xuat hang, 1: nhap hang  duoi goc nhin shop_id

    @property
    def to_json(self):
        return{
            "id": self.id,
            "customer": self.customer,
            "shop": self.shop,
            "is_export": self.is_export,
            "is_paid": self.is_paid,
            "total_amount": self.total_amount,
            "invoice_details": self.invoice_details,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "type": self.type
        }

    
class InvoiceDetail(BaseModel):
    __tablename__ = 'invoice_detail'
    id = Column(Integer,primary_key=True, )
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"),nullable=False)
    invoice_id = Column(Integer, ForeignKey("invoice.id", ondelete="CASCADE"),nullable=False)
    quantity = Column(Double, nullable=False)
    invoice = relationship('Invoice', back_populates="invoice_details")
    price = Column(Double, nullable=False)
    total = Column(Double, nullable=False, server_default="0")

    
    
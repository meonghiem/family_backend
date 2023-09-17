from pydantic import BaseModel

class InvoiceDetailType(BaseModel):
    product_id: int
    quantity: float
    price: float

class InvoiceDetailCreateModel(InvoiceDetailType):
    invoice_id: int

class InvoiceDetailUpdateModel(InvoiceDetailType):
    id: int

class InvoiceModel(BaseModel):
    customer_id: int
    shop_id: int
    is_export: bool | None
    is_paid: bool | None
    type: int | None

class InvoiceCreateModel(BaseModel):
    invoice: InvoiceModel
    invoice_details: list[InvoiceDetailType]

class InvoiceUpdateModel(BaseModel):
    id: int
    invoice: InvoiceModel
    invoice_details: list[InvoiceDetailUpdateModel]


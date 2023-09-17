from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.ext.asyncio import AsyncSession
from src.controllers.invoices.invoice_schema import InvoiceCreateModel
from src.controllers.invoices import invoice_service
from src.db import get_session

router = APIRouter()

@router.post("/invoice")
async def create(
    data: InvoiceCreateModel,
    db: AsyncSession= Depends(get_session),
    auth: AuthJWT = Depends()
):
    invoice_details = data.invoice_details
    invoice = data.invoice
    invoiceId = await invoice_service.create_invoice(db, invoice)
    await invoice_service.create_invoice_detail(db, invoiceId, invoice_details)
    
    invoice = await invoice_service.get_invoice(db, invoiceId)    
    return invoice.to_json


from sqlalchemy import insert, select, update
from sqlalchemy.orm import selectinload
from src.models.invoice import Invoice, InvoiceDetail
from src.controllers.invoices.invoice_schema import InvoiceDetailCreateModel, InvoiceDetailUpdateModel, InvoiceModel, InvoiceUpdateModel
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.exceptions import NotFound


async def create_invoice_detail(db: AsyncSession, invoice_id:int,data: list[InvoiceDetailCreateModel]):
    listDict = []
    for value in data:
        valueDict = dict(value)
        valueDict["invoice_id"]  = invoice_id
        listDict.append(valueDict)
    stm = insert(InvoiceDetail).values(listDict)
    invoice_details = await db.execute(stm)
    await db.commit()

async def get_invoice_detail(db: AsyncSession, id: int):
    stm = select(InvoiceDetail).filter_by(id= id)
    invoice_detail = (await db.execute(stm)).scalars().first()
    return invoice_detail

async def update_invoice_detail(db:AsyncSession, data: list[InvoiceDetailUpdateModel]):
    for value in data:
        stm = update(InvoiceDetail).filter_by(id = data.id).values(
            product_id= value.product_id,
            price= value.price,
            quantity = value.quantity
            )
        await db.execute(stm)
    await db.commit()

async def create_invoice(db:AsyncSession, data:InvoiceModel):
    stm = insert(Invoice).values(dict(data))
    invoice = await db.execute(stm)
    await db.commit()
    return invoice.lastrowid

async def get_invoice(db: AsyncSession, id: int):
    stm = select(Invoice).filter_by(id= id).options(
        selectinload(Invoice.shop), 
        selectinload(Invoice.customer), 
        selectinload(Invoice.invoice_details)
        )
    invoice = (await db.execute(stm)).scalars().first()
    return invoice

async def update_invoice(db: AsyncSession, data: InvoiceUpdateModel):
    id = data.id

    invoice = await get_invoice(db, id)
    if not invoice:
        raise NotFound(message="Invoice not found")
    invoice = data.invoice
    invoice_details = data.invoice_details
    await update_invoice_detail(db, invoice_details)
    stm = update(Invoice).filter_by(id = id).values(
        dict(invoice)
    )

    await db.execute(stm)
    await db.commit()
    invoice = await get_invoice(db, id)
    return invoice

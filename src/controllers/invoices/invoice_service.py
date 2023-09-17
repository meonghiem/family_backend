

from sqlalchemy import insert, select
from src.models.invoice import Invoice, InvoiceDetail
from src.controllers.invoices.invoice_schema import InvoiceDetailCreateModel, InvoiceModel
from sqlalchemy.ext.asyncio import AsyncSession


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

async def create_invoice(db:AsyncSession, data:InvoiceModel):
    stm = insert(Invoice).values(dict(data))
    invoice = await db.execute(stm)
    await db.commit()
    return invoice.lastrowid

async def get_invoice(db: AsyncSession, id: int):
    stm = select(Invoice).filter_by(id= id)
    invoice = (await db.execute(stm)).scalars().first()
    return invoice

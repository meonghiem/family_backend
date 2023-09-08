from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, async_scoped_session
from asyncio.tasks import current_task
SQLALCHEMY_DATABASE_URL = "mysql+asyncmy://root:Cocapizza2@localhost:3306/my_study"

# echo: True => generate sql queries in console
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)

# async_scoped_session is mean one connection per one session
SeesionLocal = async_scoped_session(
    async_sessionmaker(engine, expire_on_commit=False),
    scopefunc = current_task
    )

async def get_session() -> AsyncSession:
    db = SeesionLocal() 
    try:
        yield db
    finally:
        await db.close()
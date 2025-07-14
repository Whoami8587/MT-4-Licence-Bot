from sqlalchemy import Column, Integer, String, Boolean, Date
from database.db import Base, async_session
from sqlalchemy.future import select
from datetime import date

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    uid = Column(String, unique=True)
    license_code = Column(String)
    expiry = Column(Date)
    active = Column(Boolean, default=True)

async def get_user_by_id(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

async def get_user_by_uid_and_license(uid: str, license_code: str):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.uid == uid, User.license_code == license_code)
        )
        return result.scalar_one_or_none()

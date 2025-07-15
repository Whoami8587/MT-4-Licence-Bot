add# add_mega_admin.py

import asyncio
from database.database import async_main_db
from database.models import Admin, add_admin
from sqlalchemy import select

USER_ID = 6790700233  # آیدی عددی شما

async def main():
    async with async_main_db() as session:
        result = await session.execute(select(Admin).where(Admin.user_id == USER_ID))
        existing = result.scalar_one_or_none()

        if existing:
            print("❗ کاربر از قبل وجود دارد. به‌روزرسانی به MegaAdmin انجام می‌شود...")
            existing.is_mega = True
            await session.commit()
        else:
            print("✅ کاربر جدید به عنوان MegaAdmin اضافه شد.")
            await add_admin(session, user_id=USER_ID, is_mega=True)

asyncio.run(main())

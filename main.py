import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.handlers import router as handlers_router
from bot.payments import router as payments_router
from config import TELEGRAM_BOT_TOKEN

# ساخت نمونه Bot و Dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

async def main():
    # اضافه کردن تمام روت‌های هندلر به Dispatcher
    dp.include_router(handlers_router)
    dp.include_router(payments_router)

    print("🤖 ربات در حال اجراست...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

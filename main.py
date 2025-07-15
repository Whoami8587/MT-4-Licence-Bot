import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from config import TELEGRAM_BOT_TOKEN
from bot.handlers import router as handlers_router
from bot.payments import router as payments_router

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(handlers_router)
    dp.include_router(payments_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

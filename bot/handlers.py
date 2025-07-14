from aiogram import types, Router, F
from aiogram.types import Message, CallbackQuery
from bot.utils import get_user_info, check_subscription_status

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer("👋 سلام! به ربات مدیریت لایسنس خوش اومدی.")

@router.message(F.text == "/myinfo")
async def user_info_handler(message: Message):
    info = await get_user_info(message.from_user.id)
    await message.answer(info)

@router.message(F.text == "/status")
async def status_handler(message: Message):
    status = await check_subscription_status(message.from_user.id)
    await message.answer(f"وضعیت اشتراک شما: {status}")

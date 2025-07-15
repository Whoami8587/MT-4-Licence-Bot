from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("buy"))
async def handle_payment(message: Message):
    await message.answer("درگاه پرداخت به‌زودی فعال خواهد شد.")

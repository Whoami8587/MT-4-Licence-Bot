from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("سلام! به ربات خوش آمدید.")

@router.message(F.text)
async def echo_handler(message: Message):
    await message.answer(f"گفتی: {message.text}")

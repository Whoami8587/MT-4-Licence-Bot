from aiogram import Router
from aiogram.types import Message, PreCheckoutQuery, SuccessfulPayment
from config import ZARINPAL_GATEWAY_URL

router = Router()

@router.message(commands=["buy"])
async def buy_handler(message: Message):
    await message.answer("💳 لینک پرداخت شما:")
    await message.answer(f"{ZARINPAL_GATEWAY_URL}?uid={message.from_user.id}")

@router.pre_checkout_query()
async def pre_checkout_handler(query: PreCheckoutQuery):
    await query.answer(ok=True)

@router.message(SuccessfulPayment())
async def success_handler(message: Message):
    await message.answer("✅ پرداخت با موفقیت انجام شد!")

from database.models import get_user_by_id

async def get_user_info(user_id: int) -> str:
    user = await get_user_by_id(user_id)
    if not user:
        return "❌ اطلاعاتی یافت نشد."
    return f"👤 نام: {user.name}\n🆔 UID: {user.uid}\n⏳ انقضا: {user.expiry}"

async def check_subscription_status(user_id: int) -> str:
    user = await get_user_by_id(user_id)
    if not user:
        return "نامشخص"
    return "فعال ✅" if user.active else "غیرفعال ❌"

import os
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# خواندن مقادیر مورد نیاز
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ZARINPAL_GATEWAY_URL = os.getenv("ZARINPAL_GATEWAY_URL")
DATABASE_URL = os.getenv("DATABASE_URL")

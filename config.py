import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GIGACHAT_API_KEY = os.getenv('GIGACHAT_API_KEY')
YANDEX_API_KEY = os.getenv('YANDEX_API_KEY')

print('TELEGRAM_BOT_TOKEN:', TELEGRAM_BOT_TOKEN)

GIGACHAT_API_KEY = os.getenv('GIGACHAT_API_KEY')
YANDEX_API_KEY = os.getenv('YANDEX_API_KEY') 
from os import getenv
from dotenv import load_dotenv, find_dotenv
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# find the .env file and load it 
load_dotenv(find_dotenv())
# access environment variable 
bot_token = getenv("BOT_TOKEN")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=bot_token)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Хэндлер на команду /start
@dp.message(Command("keke"))
async def cmd_start(message: types.Message):
    await message.answer("Hello keke!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
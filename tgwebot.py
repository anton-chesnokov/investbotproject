import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import logging

log = logging.Logger('bot-sync-log')
dp = Dispatcher()

# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет, я инвестиционный бот")

# Run the bot
async def main() -> None:
    load_config()
    TOKEN = os.getenv("BOT_TOKEN")
    if TOKEN is None:
        log.error('BOT_TOKEN not set')
        return
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

def load_config() -> None:
    try:
        with open('.env') as config_file:
            for line in config_file:
                key : str = line[:line.index('=')]
                value : str =  line[line.index('=')+1:]
                os.environ[key] = value
    except Exception as e:
        log.error('Error reading file', e)


if __name__ == "__main__":
    asyncio.run(main())

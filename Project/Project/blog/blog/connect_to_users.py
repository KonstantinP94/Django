import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from secret import TOKEN
dp = Dispatcher()
bot = Bot(token=TOKEN)

@dp.message(Command("start"))
async def command_start_handler(message):
    await message.answer(
        "Я веду канал космических событий! ")


asyncio.run(dp.start_polling(bot))
# "работа" его - ничего не делать, только ожидать сообщения

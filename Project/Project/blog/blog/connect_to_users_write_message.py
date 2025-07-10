# import asyncio       # библиотека для работы с асинхронными (параллельными) функциями
# from aiogram import Bot, Dispatcher  # библиотека для бота: класс бота и класс диспетчера (управляющий класс)
# from aiogram.filters import Command
# from secret import TOKEN  # Секретный файл, полученный вами в переписке с бот-прародителем
# dp = Dispatcher()         # Создание управляющего объекта.
# bot = Bot(token=TOKEN)    # Создается объект бота с нашим паролем. Один бот - один экземпляр на токен.
# # Команду в бот необходимо вводить так: /start
# @dp.message(Command("start"))
# async def command_start_handler(message):
#     print('Ура! Мне написал', message.chat.id)
#     await message.answer(
#         "Я веду канал космических событий! https://t.me/n_esse")
# #asyncio.run(           # Запуск асинхронной функции
# #    dp.start_polling(  # диспетчер начинает обмен сообщениями, 
# #        bot))          # используя бот

# @dp.channel_post()
# async def channel_post_handler(channel_post):
#     await channel_post.answer('Я понял: ' + channel_post.text)
#     asyncio.run(dp.start_polling(bot))

# asyncio.run(
#     bot.send_message(
#         79023938, #chat_id,
#         "Привет!"))

# # "работа" его - ничего не делать, только ожидать сообщения

import asyncio
from datetime import datetime, timedelta
import re

# Регулярное выражение для упрощенного анализа сообщений формата
pattern = r'(разбуди|напоминание)\s+(меня\s*)?(завтра|через (\d+)\s*(день|неделю))\s*в\s*(\d+)(:\d+)?'

# Функция для чтения сообщения и извлечения даты и времени
def parse_message(text):
    match = re.match(pattern, text)
    if not match:
        raise ValueError('Сообщение не соответствует ожидаемому формату.')
    
    _, _, day_type, days, _, hour, minute = match.groups()
    
    if minute is None:
        minute = ':00'
    
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    
    if day_type == 'завтра':
        when = tomorrow.replace(hour=int(hour), minute=int(minute.strip(':')), second=0)
    elif day_type == 'через':  # Через n дней или недель
        num_days = int(days)
        future_day = today + timedelta(days=num_days * (7 if match.group(5) == 'неделю' else 1))
        when = future_day.replace(hour=int(hour), minute=int(minute.strip(':')), second=0)
    else:
        raise ValueError('Неправильный формат времени')
    
    return when

# Функция для вывода уведомления после задержки
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# Основная функция
async def main():
    messages = [
        "разбуди меня завтра в 8 часов утра",
        "напоминание через две недели в 10 утра",
        "разбуди меня завтра в полдень"
    ]

    tasks = []
    async with asyncio.TaskGroup() as tg:
        for msg in messages:
            try:
                alarm_time = parse_message(msg)
                now = datetime.now()
                
                # Если задача назначена раньше текущего времени, сдвигаемся вперед
                if alarm_time <= now:
                    alarm_time += timedelta(days=1)
                    
                delay = (alarm_time - now).total_seconds()
                task_name = f"Привет! Время просыпаться ({msg})"
                tasks.append(tg.create_task(say_after(delay, task_name)))
            
            except Exception as e:
                print(f"Ошибка обработки сообщения '{msg}': {e}")
    
    print("Все задачи завершены.")

# Запуск основной программы
asyncio.run(main())
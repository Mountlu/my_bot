import logging 
from aiogram import Bot, Dispatcher, executor, types  
import markups as nav 
import random
 
TOKEN = "7020597798:AAGhv-EzyiM8FuG5RbqKYvj1lcTt9jlL86g"
 
async def start():
    bot = Bot(token = TOKEN)  
    dp = Dispatcher(bot) 

menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
menu_keyboard(
    types.InlineKeyboardButton("Раздел 1", callback_data="section_1"),
    types.InlineKeyboardButton("Раздел 2", callback_data="section_2"),
    types.InlineKeyboardButton("Раздел 3", callback_data="section_3")

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message): 
    await message.reply('Привет! Я бот!')

@dp.message_handler(commands=['help'])
async def command_start(message: types.Message): 
    await bot.send_message("Выберите раздел", reply_markup=menu_keyboard)

@dp.callback_query_handler(lambda c: c.data == "section_1")
async def show_section_1_menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"Вы выбрали раздел {section}")

@dp.callback_query_handler(lambda c: c.data in ("section_1_item"))
async def process_menu_selection(callback_query: types.CallbackQuery):
    section = callback_query.data.split("_")[1]
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"Вы выбрали раздел {section}")

@dp.message_handler() 
async def bot_message(message: types.Message): 
    if message.text == "Рандомное число":
        await bot.send_message(message.from_user.id, "Ваше число: ",str(random.randint(0,9999)))
    elif message.text == "Главное меню":
        await bot.send_message(message.from_user.id, "Главное меню", reply_markup = nav.mainMenu)
    elif message.text == "Другое":
        await bot.send_message(message.from_user.id, "Другое", reply_markup = nav.otherMenu)
    elif message.text == "Информация":
        await bot.send_message(message.from_user.id, "Какая-то информация")
    elif message.text == "Курсы валют":
        await bot.send_message(message.from_user.id, "Курсы валют")

    else:
        await message.reply("Неизвестная команда", reply_markup = nav.mainMenu) 

    try:
        await dp_start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':  
    executor.start_polling(dp, skip_updates = True)

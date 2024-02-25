import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery
from aiogram.utils.markdown import hbold

from bot.keyboards.inline import get_main_menu, MediaInfo, get_delete_menu
from bot.utils.commands import set_commands
from bot.handlers.form import UrlForm
from parser.parser import reels, post
from TOKEN import TOKEN

dp = Dispatcher()


# Start button handler
@dp.message(CommandStart())
async def start(message: types.Message, bot: Bot, state: FSMContext):
    await set_commands(bot)
    logo = FSInputFile('bot/media/start.png')
    await message.answer_photo(photo=logo,
                               caption='Welcome to ' + hbold('Instagram Downloader 👋') +
                                       f'\n\nUsing this bot, you can download Instagram videos without watermark.')
    # Open main menu and set empty state
    await menu(message, state)
    await state.set_state(None)


# Menu button handler
@dp.message(Command('menu'))
async def menu(message: types.Message, state: FSMContext):
    await message.answer(hbold('❔What do you want to download❔'), reply_markup=get_main_menu())
    await state.set_state(None)


# If inline button 'Reel' clicked
@dp.callback_query(MediaInfo.filter(F.type == 'reel'))
async def callback_handler(call: CallbackQuery, state: FSMContext):
    # Instructions
    await call.message.answer(hbold('Enter link on reel:'))
    # Changing state
    await state.set_state(UrlForm.GET_REEL)
    await call.answer()


# Reel state handler
@dp.message(UrlForm.GET_REEL)
async def process_reel(message: types.Message):
    try:
        await message.answer_video(reels(message.text), reply_markup=get_delete_menu(deletable=False))
    except Exception:
        await message.answer('Wrong URL or video tagged 18+', reply_markup=get_delete_menu(deletable=True))


# If inline button 'Post' clicked
@dp.callback_query(MediaInfo.filter(F.type == 'post'))
async def callback_handler(call: CallbackQuery, state: FSMContext):
    # Instructions
    await call.message.answer(hbold('Simply copy link on post and enter to bot'))
    # Changing state
    await state.set_state(UrlForm.GET_POST)
    await call.answer()


# Post state handler
@dp.message(UrlForm.GET_POST)
async def process_post(message: types.Message):
    try:
        # Get all photos (list)
        photos = post(message.text)
        for photo in photos:
            # Find index for each photo
            index = photos.index(photo)
            # If index is last in list (photos) - create inline menu
            if index == len(photos) - 1:
                await message.answer_photo(photo, reply_markup=get_delete_menu(deletable=False))
            else:
                await message.answer_photo(photo)
    except Exception:
        await message.answer('Wrong URL', reply_markup=get_delete_menu(deletable=True))


# Menu inline button handlers
@dp.callback_query(MediaInfo.filter(F.type.in_(['delete_menu', 'save_menu'])))
async def callback_query(call: CallbackQuery, state: FSMContext, callback_data: MediaInfo):
    message = call.message
    # Open main menu
    await menu(message, state)
    await call.answer()
    # If deletable is True
    if callback_data.type == 'delete_menu':
        await message.delete()


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

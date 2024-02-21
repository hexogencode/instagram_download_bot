import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery
from aiogram.utils.markdown import hbold

from bot.keyboards.inline import get_inline_start, MediaInfo, get_inline_menu
from bot.utils.commands import set_commands
from bot.handlers.form import UrlForm
from parser.parser import reels
from TOKEN import TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message, bot: Bot, state: FSMContext):
    await set_commands(bot)
    logo = FSInputFile('bot/media/start.png')
    await message.answer_photo(photo=logo,
                               caption='Welcome to ' + hbold('Instagram Downloader 👋') +
                                       f'\n\nUsing this bot, you can download Instagram videos without watermark.'
                                       f'\n\nTo start downloading, please select which type you want to download.',
                               reply_markup=get_inline_start())
    await state.set_state(None)


@dp.callback_query(MediaInfo.filter(F.type.in_(['delete_menu', 'save_menu'])))
async def callback_query(call: CallbackQuery, state: FSMContext, bot: Bot, callback_data: MediaInfo):
    message = call.message
    await start(message, bot=bot, state=state)
    await call.answer()
    if callback_data.type == 'delete_menu':
        await message.delete()


@dp.callback_query(MediaInfo.filter(F.type == 'reel'))
async def callback_handler(call: CallbackQuery, state: FSMContext):
    # Instructions
    instruction = FSInputFile('bot/media/reel_screenshot.jpg')
    await call.message.answer_photo(photo=instruction, caption=hbold('Simply copy link on reel and enter to bot'))
    # State of GET_URL changes
    await state.set_state(UrlForm.GET_URL)
    await call.answer()


@dp.message(UrlForm.GET_URL)
async def process_name(message: types.Message):
    try:
        await message.answer_video(reels(message.text), reply_markup=get_inline_menu(deletable=False))
    except Exception:
        await message.answer('Wrong URL or video tagged 18+', reply_markup=get_inline_menu(deletable=True))


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

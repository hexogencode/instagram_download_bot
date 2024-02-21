# from bot.handlers.callback import MediaInfo
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MediaInfo(CallbackData, prefix='media'):
    type: str


def get_inline_start():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Reel 📹', callback_data=MediaInfo(type='reel').pack()),
        InlineKeyboardButton(text='Post 📷', callback_data=MediaInfo(type='post').pack()),
        width=2
    )
    return builder.as_markup()


def get_inline_menu(deletable: bool):
    builder = InlineKeyboardBuilder()
    if deletable:
        choice = 'delete_menu'
    else:
        choice = 'save_menu'

    builder.row(
        InlineKeyboardButton(text='MENU⬆️', callback_data=MediaInfo(type=choice).pack())
    )
    return builder.as_markup()

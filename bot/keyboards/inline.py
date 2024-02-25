# Inline buttons
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MediaInfo(CallbackData, prefix='media'):
    type: str


# Main menu buttons
def get_main_menu():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Reel 📹', callback_data=MediaInfo(type='reel').pack()),
        InlineKeyboardButton(text='Post 📷', callback_data=MediaInfo(type='post').pack()),
        InlineKeyboardButton(text='Developer', url="https://t.me/hexogen999"),
        width=2
    )
    return builder.as_markup()


# Go to menu buttons
def get_delete_menu(deletable: bool):
    builder = InlineKeyboardBuilder()
    if deletable:
        choice = 'delete_menu'
    else:
        choice = 'save_menu'
    # Different callbacks for deletable option
    builder.row(
        InlineKeyboardButton(text='MENU⬆️', callback_data=MediaInfo(type=choice).pack())
    )
    return builder.as_markup()

# File to create state handler
from aiogram.fsm.state import State, StatesGroup


class UrlForm(StatesGroup):
    GET_REEL = State()
    GET_POST = State()

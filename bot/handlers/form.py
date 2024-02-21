from aiogram.fsm.state import State, StatesGroup


class UrlForm(StatesGroup):
    GET_URL = State()
# Create command list
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='menu',
            description='Main menu'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())

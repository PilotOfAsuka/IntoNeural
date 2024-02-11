# handlers.py
import config
from misc import dp
from aiogram.types import Message
from aiogram.filters import Command
# from n_network.make_dict import training_model
# from n_network.generating import generate_from


async def save_to_file(msg: Message):
    if msg.text is not None:
        with open(config.msg_dir, 'a') as file:
            file.write(f"{msg.text}\n")


@dp.message(Command("start"))
async def start_command(msg: Message):
    await msg.answer(config.start_msg)


@dp.message()
async def message_handler(msg: Message):
    await save_to_file(msg)

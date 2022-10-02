# Powered By @panipuri

from typing import Union, List
from pyrogram import filters
from panipuri.utilities.config import COMMAND_PREFIXES


# ╔══╗╔══╗╔══╗╔══╗╔═╦╗╔══╗╔═╗╔╗─╔══╗╔═╦╗╔═╗╔═╗
# ║╔╗║╚╗╗║╚║║╝╚╗╔╝╚╗║║║╔╗║║╬║║║─║╔╗║╚╗║║║╦╝║╬║
# ║╠╣║╔╩╝║╔║║╗─║║─╔╩╗║║╠╣║║╔╝║╚╗║╠╣║╔╩╗║║╩╗║╗╣
# ╚╝╚╝╚══╝╚══╝─╚╝─╚══╝╚╝╚╝╚╝─╚═╝╚╝╚╝╚══╝╚═╝╚╩╝

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)

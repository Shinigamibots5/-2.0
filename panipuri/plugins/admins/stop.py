from pyrogram import filters
from pyrogram.types import Message

from panipuri import bot
from panipuri.utilities.config import BANNED_USERS
from panipuri.utilities.strings import get_command
from panipuri.utilities.events.command import command
from panipuri.modules.core.call import dudu
from panipuri.modules.database import set_loop
from panipuri.modules.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@bot.on_message(
    command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await dudu.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )

from pyrogram import filters
from pyrogram.types import Message

from panipuri.utilities.config import BANNED_USERS
from panipuri.utilities.strings import get_command
from panipuri.utilities.events.command import command
from panipuri import bot
from panipuri.modules.core.call import dudu
from panipuri.modules.database import is_music_playing, music_off
from panipuri.modules.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@bot.on_message(
    command(PAUSE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await dudu.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention)
    )

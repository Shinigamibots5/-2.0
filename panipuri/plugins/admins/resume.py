from pyrogram import filters
from pyrogram.types import Message

from panipuri.utilities.config import BANNED_USERS
from panipuri.utilities.strings import get_command
from panipuri.utilities.events.command import command
from panipuri import bot
from panipuri.modules.core.call import dudu
from panipuri.modules.database import is_music_playing, music_on
from panipuri.modules.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@bot.on_message(
    command(RESUME_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await dudu.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention)
    )

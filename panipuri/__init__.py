# dudu PLAYER

from panipuri.modules.core.app import App
from panipuri.modules.core.bot import Bot
from panipuri.modules.core.dir import dirr
from panipuri.modules.core.git import git
from panipuri.misc import dbb, heroku, sudo

from .console import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
bot = Bot()

# Assistant Client
app = App()

from panipuri.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

#
# Copyright (C) 2021-2022 by The_Shadow_Knight@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @The_Shadow_Knight
# Rocks © @OFFICIALBOT_SUPPORT
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alexa © Yukki


from AlexaMusic.core.bot import AlexaBot
from AlexaMusic.core.dir import dirr
from AlexaMusic.core.git import git
from AlexaMusic.core.userbot import Userbot
from AlexaMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

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
app = AlexaBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

# dudu dudu
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

from panipuri.utilities import config
from panipuri.console import LOGGER

TEMP_MONGODB = "mongodb+srv://ticel98214:asdfggjkl@cluster0.hm6jsk4.mongodb.net/?retryWrites=true&w=majority"


if config.MONGO_DB_URL is None:
    LOGGER(__name__).warning(
        "๐ฅ ๐๐จ ๐๐จ๐ง๐ ๐จ ๐๐ ๐๐ซ๐ฅ ๐๐จ๐ฎ๐ง๐ โจ...\n\n๐น ๐๐จ๐ฎ๐ซ ๐๐จ๐ญ ๐๐ข๐ฅ๐ฅ ๐๐จ๐ซ๐ค ๐๐ง\nเคชเคพเคจเฅเคชเฅเคฐเฅ 2.0'๐ฌ ๐๐๐ญ๐๐๐๐ฌ๐ โจ ..."
    )
    temp_client = Client(
        "dudu",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URL)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URL)
    mongodb = _mongo_async_.dudu
    pymongodb = _mongo_sync_.dudu

# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 1234567))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Footer-Bot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    START_TEXT = """
مرحبا بك في بوت تعديل حقوق القناة
انا اقوم بوضع رابط او نص تلقائيا اخر أي منشور بالقناه 
فقط قم بوضعي مشرف مع اعطائي الصلاحيات 
ثم ارسل بالقناه الامر /settings"""

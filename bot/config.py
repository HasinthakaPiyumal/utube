import os


class Config:

    BOT_TOKEN = "2070291678:AAFn6SaTbUP9f3BXdjw16PiuhVNlOeKu9Lg"

    SESSION_NAME = "YoutubeUpHasibot"

    API_ID = 10052403

    API_HASH = "4e3763b6bbdd98f712a2e3b000defd11"

    CLIENT_ID = "924713315459-h1ed1fol5403ri6tpvhu6fl2ujc9nk08.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = 1766930243

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"

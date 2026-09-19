import os

# Telegram Bot sozlamalari
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "6526744258"))

# Xotira kanali ID si (buni keyingi qadamda olamiz)
CHANNEL_ID = os.getenv("CHANNEL_ID", "")

# AI kaliti (buni ham bepul olamiz)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

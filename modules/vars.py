import os

API_ID    = os.environ.get("API_ID", "10768857")
API_HASH  = os.environ.get("API_HASH", "81b5d675d410f16ceb39df10db9cdb54")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7464498219:AAFacXLo-pvsNBWog8jgXtd3YU0pLukVvJ0") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

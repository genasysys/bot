import os

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN muhit o'zgaruvchisi o'rnatilmagan!")

# Admin IDlar (vergul bilan ajrating: 123456,789012)
ADMIN_IDS = []
admin_id = os.environ.get("ADMIN_ID", "")
if admin_id:
    try:
        ADMIN_IDS = [int(x.strip()) for x in admin_id.split(",") if x.strip()]
        print(f"✅ {len(ADMIN_IDS)} ta admin yuklandi: {ADMIN_IDS}")
    except ValueError:
        print("⚠️ ADMIN_ID noto'g'ri formatda! Masalan: 123456,789012")

if not ADMIN_IDS:
    print("⚠️ Hech qanday admin aniqlanmadi!")

# Database fayl yo'li
DB_FILE = "data/database.json"

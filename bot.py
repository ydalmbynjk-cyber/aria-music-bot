from rubpy import Client
import re

bot = Client("my_session")

FORBIDDEN_PATTERN = re.compile(
    r'(https?://|www\.|rubika\.ir/|t\.me/|telegram\.me/|instagram\.com/|@\w+)',
    re.IGNORECASE
)

@bot.on_message_updates()
async def handler(message):
    if not message.object_guid.startswith("g0"):
        return

    text = message.text or ""

    if text and FORBIDDEN_PATTERN.search(text):
        try:
            await message.delete()
            await message.reply("🚫 ارسال لینک و آیدی در این گروه ممنوع است.")
        except:
            pass
        return

    greetings = {
        "سلام": "سلام! 🌟 وقتتون بخیر، خوش اومدید.",
        "صبح بخیر": "صبح بخیر ☀️ روزتون پر از انرژی باشه!",
        "شب بخیر": "شب بخیر 🌙 خواب‌های قشنگ ببینید.",
        "جیگر": "جیگر ❤️ چطوری؟",
        "ایولا": "ایول 🔥 دمت گرم!",
        "مانده": "مانده‌ای؟ 😅 چیزی شده؟",
    }

    if text.strip() in greetings:
        await message.reply(greetings[text.strip()])

bot.run()

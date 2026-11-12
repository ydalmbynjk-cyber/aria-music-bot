from rubpy import Bot
import re

# توکن ربات خود را اینجا وارد کنید (یا اگر از کلاینت استفاده می‌کنید)
# برای ربات‌های رسمی روبیکا از Bot استفاده می‌شود
bot = Bot('YOUR_BOT_TOKEN')

FORBIDDEN_PATTERN = re.compile(
    r'(https?://|www\.|rubika\.ir|t\.me)',
    re.IGNORECASE
)

@bot.on_message_updates()
async def handler(event):
    try:
        text = event.text or ""
        if text and FORBIDDEN_PATTERN.search(text):
            await event.delete()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    bot.run()
    

from rubpy import Client
import time
import re

# راه‌اندازی کلاینت با توکن شما
client = Client('CJBDDJ0JLODRJGHHIBUXTTMOVCFWVDTTAWNLLRSHEIGZYKOOTVNKSBYBVVBVQGTT')

FORBIDDEN_PATTERN = re.compile(
    r'(https?://|www\.|rubika\.ir|t\.me)',
    re.IGNORECASE
)

@client.on_message_updates()
async def anti_link(event):
    try:
        text = event.text or ""
        if text and FORBIDDEN_PATTERN.search(text):
            await event.delete()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Bot is starting up...")
    try:
        client.run()
    except Exception as e:
        print(f"Runtime error: {e}")
        # یک حلقه تنفس برای اینکه سرور رندر بسته نشود
        while True:
            time.sleep(60)
            

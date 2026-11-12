from rubpy import Client
import asyncio
import re

async def main():
    # مقداردهی کلاینت با توکن شما
    client = Client('CJBDDJ0JLODRJGHHIBUXTTMOVCFWVDTTAWNLLRSHEIGZYKOOTVNKSBYBVVBVQGTT')
    
    # تنظیم الگو برای پیدا کردن لینک‌ها و آدرس‌ها
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
            print(f"Error handling message: {e}")

    print("Bot is starting and listening for messages...")
    
    # شروع به کار ربات به صورت پایدار در لوپ رویداد
    await client.run()

if __name__ == "__main__":
    asyncio.run(main())
    

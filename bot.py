from rubpy import Client
import asyncio
import re

bot = Client("my_session")

FORBIDDEN_PATTERN = re.compile(
    r'(https?://|www\.|rubika\.ir|t\.me)',
    re.IGNORECASE
)

@bot.on_message_updates()
async def handler(message):
    if not message.object_guid.startswith('g'):
        return

    text = message.text or ""

    if text and FORBIDDEN_PATTERN.search(text):
        try:
            await message.delete()
        except Exception:
            pass

async def main():
    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
    

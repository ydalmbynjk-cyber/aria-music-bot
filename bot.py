from rubpy import Client
import asyncio
import re

async def main():
    bot = Client("my_session")
    
    FORBIDDEN_PATTERN = re.compile(
        r'(https?://|www\.|rubika\.ir|t\.me)',
        r
    

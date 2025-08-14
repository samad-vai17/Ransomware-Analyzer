# Get_key.py
import time
import threading
from Telegram_Bot import run_bot
from Telegram_Bot import get_last_key
import asyncio

# 8/14/2025
# Get Key from Bot Code
# AUX-441


def start_bot_in_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())
    loop.run_forever()


bot_thread = threading.Thread(target=start_bot_in_thread, daemon=True)
bot_thread.start()

def key():
    while True:
        k = get_last_key()
        if k is not None:
            return k.decode()
        print("Waiting For key ...")
        time.sleep(5)







import asyncio
import os
import time
import random

"""
    This is an example of how to schedule an IO-bound sync
    func on an event loop in asyncio to achieve concurrency
"""

def sync_dl(file):
    time.sleep(random.randint(0,15))
    print('Starting:', file)
    # Do IO-bound task here
    time.sleep(1)
    print('Done:', file)

async def dl_file(file):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, sync_dl, file)

async def main(files):
    tasks = []
    for file in files:
        tasks.append(dl_file(file))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    with open('files') as f:
        files = f.read().splitlines()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(files))
    loop.close()
import asyncio
import time


async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    start = time.perf_counter()
    # print("Hello")
    # await asyncio.sleep(1)
    # print('... world')
    all = [add(2,3),add(12,3),add(2,3),add(12,3),add(2,3),add(12,3),add(2,3),add(12,3),add(2,3),add(12,3)]
    results = await asyncio.gather(*all)
    end = time.perf_counter()

    print(results)
    print(end-start)

if __name__=='__main__':
    asyncio.run(main())

import asyncio


async def hello_world():
    print("Started 🌍")
    await asyncio.sleep(1)
    print("Hello, sanlam 🌍")


asyncio.run(hello_world())


# Task 1: Happy new year count down
async def happy_new_year():
    print("3")
    await asyncio.sleep(1)
    print("2")
    await asyncio.sleep(1)
    print("1")
    await asyncio.sleep(1)
    print("Happy New Year 🎊")


asyncio.run(happy_new_year())


# Task 2: Make task 1 DRY: Create a reusable async function
async def happy_new_year2(n):
    for i in range(n, 0, -1):
        print(i)
        await asyncio.sleep(1)
    print("Happy New Year 🎊")


asyncio.run(happy_new_year2(3))


# Task 3: Do task 2 without any loop
# DRY: Create a reusable async function
async def happy_new_year3(n):
    print(n)
    await asyncio.sleep(1)
    if n == 1:
        print("Happy New Year 🎊")


asyncio.run(happy_new_year3(3))
asyncio.run(happy_new_year3(2))
asyncio.run(happy_new_year3(1))


async def count_and_sleep(msg):
    print(msg)
    await asyncio.sleep(1)  # sleep -> inbuilt async function


async def countdown():
    await count_and_sleep("3")  # sync
    await count_and_sleep("2")
    await count_and_sleep("1")
    await count_and_sleep("Happy New Year 🎊")


# Every aync function returns a coroutine

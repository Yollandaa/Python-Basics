import asyncio


# # async def background_task():
# #     print("Start Background Task")
# #     await asyncio.sleep(3)

# # Async no event loop
# # async def main():
# #     await background_task()
# #     print("Main function says - Hi")


# # asyncio.run(main())
# # We don't want the await background task


# # This one first prints all the mains and prints the background_task after the main are done
# # This happens concurrently
# async def cooking_eggs():
#     print("Eggs cooking")
#     await asyncio.sleep(3)
#     print(
#         "Eggs cooked"
#     )  # does not see this print statement because the main task is done
#     return f"Data - Eggs 🥚"


# async def make_coffee():
#     print("Coffee brewing")
#     await asyncio.sleep(2)
#     print("Coffe done")
#     return f"Data - Coffee ☕"


# async def make_cereal():
#     print("Making Cereal bowl")
#     await asyncio.sleep(5)
#     print("Cereal done")
#     return f"Data - Cereal 🥣"


# async def main():
#     # Request to event loop to schedule
#     task1 = asyncio.create_task(cooking_eggs())  # happens concurrently
#     task2 = asyncio.create_task(make_coffee())  # happens concurrently
#     # Waiting for the background task
#     print("Main function says - Hi")
#     print("Main function says - Hi")
#     print("Main function says - Hi")

#     # await task1  # This waits for the eggs_cooking task to finish

#     # What if we do not know the longest task is: Wait for all tasks to finish (a set of tasks)
#     await asyncio.wait({task1, task2})


# # asyncio.run(main())


# # # Using gather
# # async def main():
# #     # Request to event loop to schedule
# # The schedule is happening
# #     all_tasks = [
# #         asyncio.create_task(cooking_eggs()),
# #         asyncio.create_task(make_coffee()),
# #         asyncio.create_task(make_cereal()),
# #     ]
# #     # Waiting for the background task
# #     print("Main function says - Hi 1")
# #     print("Main function says - Hi 2")
# #     print("Main function says - Hi 3")

# #     # await task1  # This waits for the eggs_cooking task to finish
# #     data = await asyncio.gather(*all_tasks)  # Unpacking the tasks
# #     print(data)


# # asyncio.run(main())

# # Another way to do it


# # All async functions return a coroutine object
# # We use gather cuz you don't need to say create_task
# async def main():
#     # No scheduling is happening here
#     all_co_routines = [
#         cooking_eggs(),
#         make_coffee(),
#         make_cereal(),
#     ]

#     # Waiting for the background task
#     print("Main function says - Hi 1")
#     print("Main function says - Hi 2")
#     print("Main function says - Hi 3")

#     await asyncio.sleep(10)

#     # Scheduling is only triggered here with the gather
#     data = await asyncio.gather(*all_co_routines)  # Unpacking the tasks
#     print(data)


# asyncio.run(main())


async def timer(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} is done after {delay}")
    return f"Data - {name}"


async def main():
    output = await asyncio.gather(timer("slow task", 3), timer("fast task", 1))
    print(output)


asyncio.run(main())

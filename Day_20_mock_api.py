from pprint import pprint
import asyncio
import aiohttp


async def get_users():
    url = "https://65f8285ab4f842e80887137c.mockapi.io/users"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            users = await response.json()
            return users


# async def main():
#     names = [user["name"] for user in await get_users()]
#     # pprint(names)
#     print("\n".join(names))


# asyncio.run(main())

# Delete user with 15 using async


async def delete_user(user_id):
    url = f"https://65f8285ab4f842e80887137c.mockapi.io/users/{user_id}"
    async with aiohttp.ClientSession() as session:
        async with session.delete(url) as response:
            users = await response.json()
            return users


# delete the first 5 users
# async def main():
#     # print the users first
#     users = await get_users()
#     for user in users:
#         print(user["name"])

#     # get the first 5 ids from the users list using list comprehension
#     ids_co_routines = [delete_user(user["id"]) for user in users[:5]]
#     id_data = await asyncio.gather(*ids_co_routines)

#     print("--------------------------------------")
#     # print the users after
#     users_after = await get_users()
#     for user in users_after:
#         print(user["name"])


# asyncio.run(main())


# Task 2: Change all users' avaters to human rights flag
async def change_avatar(user_id, data):
    url = f"https://65f8285ab4f842e80887137c.mockapi.io/users/{user_id}"
    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=data) as response:
            users = await response.json()
            return users


async def main():
    # get all the users: for each user change avatar key to
    users = await get_users()
    avatar_url = "https://www.shutterstock.com/image-vector/human-rights-day-south-africa-600w-1937647653.jpg"
    data = {"avatar": avatar_url}

    ids_co_routines = [change_avatar(user["id"], data) for user in users]
    id_data = await asyncio.gather(*ids_co_routines)

    print(id_data)


asyncio.run(main())

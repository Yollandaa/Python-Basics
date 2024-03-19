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


# Task 1: Create a new user
async def create_user(new_user):
    url = "https://65f8285ab4f842e80887137c.mockapi.io/users"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=new_user) as response:
            users = await response.json()
            return users


# async def main():
#     # get all the users: for each user change avatar key to
#     new_user = {
#         "name": "Caleb Potts",
#         "avatar": "https://media.licdn.com/dms/image/C4D03AQHxbiuJcNSm3w/profile-displayphoto-shrink_200_200/0/1566069760288?e=2147483647&v=beta&t=GsaCn0lHpyZZhJErdLBKSRpkUJfiNPXssyzbGc8XckI",
#     }

#     user = await create_user(new_user)
#     print(user)

# asyncio.run(main())


# Task 2: Create 5 users with the same avatar
# async def main():
#     user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
#     avatar_url = (
#         "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
#     )
#     users_data = [create_user({"name": user, "avatar": avatar_url}) for user in user_list]
#     users_gather = await asyncio.gather(*users_data)
#     print(users_gather)


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
    avatar_url = (
        "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
    )
    data = {"avatar": avatar_url}

    ids_co_routines = [change_avatar(user["id"], data) for user in users]
    id_data = await asyncio.gather(*ids_co_routines)
    print(id_data)


asyncio.run(main())

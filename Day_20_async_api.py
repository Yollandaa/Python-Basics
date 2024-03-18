from pprint import pprint
import asyncio
import aiohttp

TOKEN = "fb838521799749b48ad93208241503"


async def get_city_temp(city_name):
    print(f"Getting temp of {city_name}")
    await asyncio.sleep(2)
    url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
    # Memory management - Error
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            print(
                f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']}°C"
            )


# async def main():
#     await get_city_temp("Chennai")
#     await get_city_temp("Johannesburg")
#     await get_city_temp("Durban")


# Task 1: Use gather to make the API time faster
# main function with gather
# async def main():
#     all_co_routine = [
#         get_city_temp("Chennai"),
#         get_city_temp("Johannesburg"),
#         get_city_temp("Durban"),
#     ]

# Each element is passed an an argument
#     await asyncio.gather(*all_co_routine)


# Task 2: Now use gather and create_task to make the API time faster
# async def main():
#     tasks = [
#         asyncio.create_task(get_city_temp("Chennai")),
#         asyncio.create_task(get_city_temp("Johannesburg")),
#         asyncio.create_task(get_city_temp("Durban")),
#     ]
#     await asyncio.gather(*tasks)


# asyncio.run(main())


# Task 3: Make task 2 DRY
cities = [
    "New York",
    "Tokyo",
    "London",
    "Paris",
    "Dubai",
    "Singapore",
    "Sydney",
    "Istanbul",
    "Hong Kong",
    "Cape Town",
]


# async def main():
#     all_co_routines = [asyncio.create_task(get_city_temp(city)) for city in cities]
#     await asyncio.gather(*all_co_routines)


# asyncio.run(main())


# Task 4: Create a function that takes in a list of cities and returns the temperatures
async def get_city_temp_only(city_name):
    url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
    # Memory management - Error
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            return weather["location"]["name"], weather["current"]["temp_c"]


async def main():
    cities_data_co_current = [get_city_temp_only(city) for city in cities]
    cities_data = await asyncio.gather(*cities_data_co_current)
    pprint(dict(cities_data))


asyncio.run(main())

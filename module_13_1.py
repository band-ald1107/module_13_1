import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for ball in range(1,6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {ball} шар")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    participants = [("Pasha", 3), ("Denis", 4), ("Apollon", 5)]


    tasks = []
    for name, power in participants:
        tasks.append(start_strongman(name, power))


    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(start_tournament())

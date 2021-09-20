import asyncio
from random import random


# funkcja symulująca długie obliczenia
async def long_computation(task_id: int) -> str:
    for i in range(3):
        await asyncio.sleep(random())
        print(f"Task {task_id}: {i}")
    return "DONE"


# uruchamia n współbieżnych funkcji _long_computation_
async def launch_tasks(n_tasks: int):
    coros = [long_computation(i) for i in range(n_tasks)]
    await asyncio.gather(*coros)


asyncio.run(launch_tasks(3))
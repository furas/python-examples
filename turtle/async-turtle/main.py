
# date: 2019.04.08
# https://stackoverflow.com/a/55564375/1832058
# see also "aioturtle": https://github.com/appeltel/aioturtle

import asyncio
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

async def jump1():
    while True:
        t1.fd(100)
        await asyncio.sleep(0.01)
        t1.left(90)


async def jump2():
    while True:
        t2.fd(100)
        await asyncio.sleep(0.01)
        t2.right(90)

tasks = [jump1(), jump2()]
asyncio.run(asyncio.wait(tasks))

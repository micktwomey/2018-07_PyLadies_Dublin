import asyncio
import contextvars
import random

message = contextvars.ContextVar("message")


async def read_message(i, msg):
    message.set(msg)
    await asyncio.sleep(i)  # pretend I'm a HTTP request
    print(f"Message for {i} is {message.get()!r} (originally {msg!r})")


async def main():
    await asyncio.gather(
        read_message(1, "ham"),
        read_message(3, "spam"),
        read_message(2, "eggs"),
        read_message(0, "foo"),
    )

    print("main done")


asyncio.run(main())
print("asyncio done")

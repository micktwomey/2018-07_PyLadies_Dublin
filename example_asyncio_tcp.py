import asyncio
import contextvars

client_addr_var = contextvars.ContextVar("client_addr")


def render_goodbye():
    client_addr = client_addr_var.get()
    return f"Good bye, client @ {client_addr}\n".encode()


async def handle_request(reader, writer):
    addr = writer.transport.get_extra_info("socket").getpeername()
    client_addr_var.set(addr)

    while True:
        line = await reader.readline()
        if not line.strip():
            break
        writer.write(f"Sleeping for {line}\n".encode())
        print(f"Sleeping for {line} seconds for client {client_addr_var.get()}")
        await asyncio.sleep(float(line))
        writer.write("Awake again\n".encode())

    print(f"Goodbye to client {client_addr_var.get()}")
    writer.write(render_goodbye())
    writer.close()


async def main():
    srv = await asyncio.start_server(handle_request, "127.0.0.1", 8081)

    async with srv:
        await srv.serve_forever()


asyncio.run(main())

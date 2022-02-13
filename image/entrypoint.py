# Copyright (C) 2022 Vladimir Berlev
#
# SPDX-License-Identifier: MIT

import asyncio
import signal


async def main():
    loop = asyncio.get_event_loop()

    shutdown = asyncio.Event()
    loop.add_signal_handler(signal.SIGTERM, shutdown.set)

    await shutdown.wait()


if __name__ == '__main__':
    asyncio.run(main())


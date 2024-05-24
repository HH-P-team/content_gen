from aiofiles import open as aopen
from aiofiles import os as aos


async def acopy(src_path, target_path):

    async with aopen(src_path, "r") as source:

        stat_src = await aos.stat(src_path)
        n_bytes = stat_src.st_size

        async with aopen(target_path, "w") as target:

            fd_src = source.fileno()
            fd_tar = target.fileno()

            await aos.sendfile(fd_tar, fd_src, 0, n_bytes)

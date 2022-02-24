import sys

if hasattr(sys.modules["__main__"], "get_ipython"):
    from tqdm import notebook as tqdm
else:
    import tqdm
from time import sleep

n = 0
for i in tqdm.trange(100):
    n += 1
    sleep(0.01)

url = "https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe"
import httpx
with httpx.stream("GET", url) as response:
    total = int(response.headers["Content-Length"])
    with tqdm.tqdm(total=total) as progress:
        for chunk in response.iter_bytes():
            progress.update(len(chunk))
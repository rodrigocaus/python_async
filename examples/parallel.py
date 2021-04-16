import requests
import concurrent.futures
from tasks import io
from util import timecount


@timecount.exectime
def call():
    print('Index,Exists')
    page = 'https://en.wikipedia.org/wiki/{}'
    futures = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(100):
            futures.append(executor.submit(
                io.page_exists, page.format(i), requests.Session()))

        concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

    for i, f in enumerate(futures):
        print(f'{i},{f.result()}')


call()

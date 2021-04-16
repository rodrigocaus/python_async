import requests
import concurrent.futures
from tasks import io
from util import timecount


@timecount.exectime
def call():
    print('Index,Exists')
    page = 'https://en.wikipedia.org/wiki/{}'
    args = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            for i in range(100):
                args.append((page.format(i), session))

            results = executor.map(lambda arg: io.page_exists(*arg), args)

    for i, res in enumerate(results):
        print(f'{i},{res}')


call()

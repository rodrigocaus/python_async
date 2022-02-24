import requests
import concurrent.futures
from tasks import io
from util import timecount


MAX_CONNECTIONS = 100

@timecount.exectime
def call():
    adapter = requests.adapters.HTTPAdapter(pool_connections=MAX_CONNECTIONS, pool_maxsize=MAX_CONNECTIONS)
    print('Index,Exists')
    page = 'https://en.wikipedia.org/wiki/{}'
    args = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONNECTIONS) as executor:
        with requests.Session() as session:
            session.mount('http://', adapter)
            for i in range(100):
                args.append((page.format(i), session))

            results = executor.map(lambda arg: io.page_exists(*arg), args)

    for i, res in enumerate(results):
        print(f'{i},{res}')


call()

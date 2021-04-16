import requests
from tasks import io
from util import timecount


@timecount.exectime
def call():
    print('Index,Exists')
    page = 'https://en.wikipedia.org/wiki/{}'
    results = []
    with requests.Session() as session:
        for i in range(100):
            results.append(io.page_exists(page.format(i), session))

    for i, res in enumerate(results):
        print(f'{i},{res}')


call()

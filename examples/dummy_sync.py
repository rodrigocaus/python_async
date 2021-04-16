import time
from util import timecount


def dummy(i: int):
    print('Begin:', i)
    # Simulate a blocking IO task
    time.sleep(i)
    print('End:', i)


@timecount.exectime
def call():
    dummy(1)
    dummy(2)
    dummy(3)


call()

from tasks import cpu
from util import timecount


@timecount.exectime
def call():
    cpu.countdown(200000000)


call()

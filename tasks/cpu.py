

def memory(n: int) -> dict:
    d = dict()
    for i in range(n):
        d[f'{i}'] = i
    return d


def countdown(n: int) -> None:
    while n > 0:
        n -= 1


def fibo(i: int) -> int:
    if i <= 0:
        return 0
    elif i in (1, 2):
        return 1

    return fibo(i - 1) + fibo(i - 2)

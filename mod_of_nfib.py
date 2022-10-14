from datetime import datetime


def get_pizano(n, m):
    pizano = -1
    prev = 0
    val = 1
    piz_handled = False
    while n > 0:
        next_val = val + prev
        piz_handled = (next_val % m == 1 and val % m == 1 and prev % m == 0 and pizano > 0)
        pizano = pizano + 1
        if piz_handled:
            break
        n = n - 1
        prev = val
        val = next_val

    return pizano if piz_handled else -1


def fib_mod(n, m):
    pizano = get_pizano(n, m)

    val = 0
    next_val = 1
    pos = (n % pizano if pizano > 0 else n)

    while pos > 0:
        pos = pos - 1
        cnt = next_val + val
        val = next_val
        next_val = cnt
    return val % m


def fib_mod_naive(n, m):
    n_val = 1
    prev = 0
    for i in range(0, n - 1):
        buf = n_val + prev
        prev = n_val
        n_val = buf
    return n_val % m


def main():
    n, m = map(int, input().split())
    start = datetime.now()
    print(fib_mod(n, m))
    t_delta = datetime.now() - start
    print(fib_mod_naive(n, m))
    print(t_delta.total_seconds())


if __name__ == "__main__":
    main()

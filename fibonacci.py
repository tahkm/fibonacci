n = int( input() )

cache = {}

def fibo_cache(n):
    global cache
    print(f'called fibo({n})')

    if n == 1:
        return 0
    elif n == 2:
        return 1

    if n in cache.keys():
        print(f'fib({n}) is in cache!, result={cache[n]}')
    else:
        cache[n] = fibo_cache(n-1) + fibo_cache(n-2)
        
    return cache[n]

def fibo(n):
    print(f'called fibo({n})')

    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fibo(n-1) + fibo(n-2)

print(fibo(n))
print('+++++++++++++++++++++++++++++++++++')
print(fibo_cache(n))


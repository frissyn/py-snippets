import timeit

def elapsed(func):
    def timed(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer() - start

        print(f"'{func.__name__}' runtime: {start - end}")

        return result
    
    return timed


@elapsed
def do_stuff():
    l = set([i for i in range(1000) if i % 2 == 0])

    return l

do_stuff()

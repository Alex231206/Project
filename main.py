def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()

        return_value = func(*args, **kwargs)
        end = time.time()

        print(f'Время выполнения: {end - start}')

        return return_value

    return wrapper


def character_counter_v0(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1

        print(f'Количество {sym}: {counter}')


def character_counter_v1(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1

        print(f'Количество {sym}: {counter}')

@benchmark
def character_counter_v2(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    return syms_counter

d = character_counter_v2('Hello, world!')
print(d)
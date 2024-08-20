# Создайте функцию генератор чисел Фибоначчи

def fib(n: int) -> list[int]:
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


print(*(fib(10)))
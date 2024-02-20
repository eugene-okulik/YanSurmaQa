def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()


def get_fibonacci_element(n):
    for i in range(n + 1):  # добавим 1, т.к. индексация идет с 0
        element = next(f)
    return element


print(get_fibonacci_element(5))
print(get_fibonacci_element(200))
print(get_fibonacci_element(1000))
print(get_fibonacci_element(100000))

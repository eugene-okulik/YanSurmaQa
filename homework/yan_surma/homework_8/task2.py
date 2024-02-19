def fibonacci():
    fib_list = []
    a, b = 0, 1
    for i in range(1, 100001):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


fibonacci_list = fibonacci()
print(fibonacci_list[4])
print(fibonacci_list[199])
print(fibonacci_list[999])
print(fibonacci_list[99999])

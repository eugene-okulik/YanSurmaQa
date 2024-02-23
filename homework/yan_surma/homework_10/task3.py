def select_operation(func):
    def wrapper(*args):
        if first == second:
            return func(first, second, '+')
        elif first < 0 or second < 0:
            return func(first, second, '*')
        elif first > second:
            return func(second, first, '-')
        elif second > first:
            return func(first, second, '/')

    return wrapper


@select_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first = int(input("Первое число: "))
second = int(input("Второе число: "))

print(calc(first, second))

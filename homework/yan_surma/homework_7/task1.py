from random import randint

secret_number = randint(1, 10)
n = int(input('Введите ваше число от 1 до 10: '))

while secret_number != n:
    print('Не угадали, попробуйте еще раз.')
    n = int(input('Введите новое число: '))
print('Поздравляю, вы угадали число!')


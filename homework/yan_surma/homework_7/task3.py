text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'


def get_number_from_text(text):
    number = int(text[text.index(':') + 2:]) + 10
    return number


num1 = get_number_from_text(text_1)
num2 = get_number_from_text(text_2)
num3 = get_number_from_text(text_3)

print(num1 + num2 + num3)

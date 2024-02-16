text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'

num_1 = int(text_1[text_1.index(':') + 2:]) + 10  # Находим вхождение : + 2 символа вперед
num_2 = int(text_2[text_2.index(':') + 2:]) + 10
num_3 = int(text_3[text_3.index(':') + 2:]) + 10

result = num_1 + num_2 + num_3
print(result)



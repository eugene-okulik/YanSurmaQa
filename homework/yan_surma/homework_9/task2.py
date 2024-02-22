temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

new_temp = filter(lambda x: x > 28, temperatures)
new_temp = list(new_temp)
print(new_temp)
print(min(new_temp))
print(max(new_temp))
average_temp = sum(new_temp) / len(new_temp)
print(round(average_temp, 2))  # Округлим до 2х знаков

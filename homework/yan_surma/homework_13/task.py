import datetime
import os

current_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(current_path))  # Выход на 2 уровня выше
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(eugene_file_path, 'r') as eugene_file:
    data = eugene_file.read()

print(data)  # Содержимое файла

dates = [line[3:29] for line in data.split('\n')]
print(dates)  # Находим даты, помещаем в список

py_dates = [datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in dates]
print(py_dates)  # Преобразуем в новый список, но уже в формате питона

date_week_later = py_dates[0] + datetime.timedelta(days=7)
print(date_week_later)  # Получаем дату на 7 дней позже от первой даты

week_day = py_dates[1].isoweekday()
print(week_day)  # День недели второй даты

new_date = (py_dates[2] - datetime.datetime.now())
days_ago = new_date.days
print(days_ago)  # Разница в днях от указанной в файле даты и текущей

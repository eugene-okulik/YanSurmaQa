import datetime

date_value = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(date_value, '%b %d, %Y - %H:%M:%S')

print(python_date.strftime('%B'))

human_date = python_date.strftime('%d.%m.%Y, %H:%M')
print(human_date)

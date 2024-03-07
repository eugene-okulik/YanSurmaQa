import csv
import os

import dotenv
import mysql.connector

current_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(current_path))
hw_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

# Записываем данные из файла
data = []
with open(hw_file_path, newline='') as csvfile:
    file_data = csv.DictReader(csvfile)
    for row in file_data:
        data.append(row)

# Подключились к бд по .venv
dotenv.load_dotenv()

db = mysql.connector.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

# Формируем запрос к БД
select_query = '''
SELECT students.name,
students.second_name,
`groups`.title,
books.title,
subjets.title,
lessons.title,
marks.value
FROM students
JOIN `groups` ON `groups`.id = students.group_id
JOIN books ON books.taken_by_student_id = students.id
JOIN marks ON marks.student_id = students.id
JOIN lessons ON lessons.id = marks.lesson_id
JOIN subjets ON subjets.id = lessons.subject_id;
'''

# Выполняем запрос
cursor.execute(select_query)
#  Получаем данные (таблицу) в полном виде
query_data = cursor.fetchall()

# Цикл, бежим по каждому обьекту и проверяем наличие данных во всей таблице
for item in data:
    if item not in query_data:
        print(f'Данных нет в таблице: {item}')
    else:
        print(f'Данные есть в таблицe: {item}')

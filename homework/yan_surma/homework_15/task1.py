import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Подготовим данные, для удобства работы с БД
name = 'Yan4'
second_name = 'Surma4'

create_student = "INSERT INTO students(name,second_name, group_id) VALUES (%s, %s, 1)"
cursor.execute(create_student, (name, second_name))
student_id = cursor.lastrowid
print(f'id студента {student_id}')

# Создаем книги
create_book1 = "INSERT INTO books(title,taken_by_student_id) VALUES('SQL and Python. Tom 1', %s)"
cursor.execute(create_book1, (student_id,))

create_book2 = "INSERT INTO books(title,taken_by_student_id) VALUES('SQL and Python. Tom 2', %s)"
cursor.execute(create_book2, (student_id,))

# Создаем группу
create_group = "INSERT INTO `groups`(title, start_date, end_date) VALUES('Video course', 'feb 2024', 'jun 2024')"
cursor.execute(create_group)
group_id = cursor.lastrowid
print(f'id группы {group_id}')

# Обновляем student_id
update_group_id = "UPDATE students SET group_id = %s WHERE students.name = %s"
cursor.execute(update_group_id, (group_id, name))

# Убедимся в обновлении данных о студенте
check_student = "SELECT name FROM students WHERE group_id = %s"
cursor.execute(check_student, (group_id,))
student_data = cursor.fetchall()
print(student_data)

# Создаем предметы
create_subject1 = cursor.execute("INSERT INTO subjets(title) VALUES ('Programming in Python.Tom 1')")
subject1_id = cursor.lastrowid
print(subject1_id)

create_subject2 = cursor.execute("INSERT INTO subjets(title) VALUES ('DATABASE with SQL. Tom 1')")
subject2_id = cursor.lastrowid
print(subject2_id)

# Создаем уроки
lesson1 = "INSERT INTO lessons(title, subject_id) VALUES ('Python lesson 1', %s)"
cursor.execute(lesson1, (subject1_id,))
lesson1_id = cursor.lastrowid
print(lesson1_id)

lesson2 = "INSERT INTO lessons(title, subject_id) VALUES ('Python lesson 2', %s)"
cursor.execute(lesson2, (subject1_id,))
lesson2_id = cursor.lastrowid
print(lesson2_id)

lesson3 = "INSERT INTO lessons(title, subject_id) VALUES ('Databases lesson 1', %s)"
cursor.execute(lesson3, (subject2_id,))
lesson3_id = cursor.lastrowid
print(lesson3_id)

lesson4 = "INSERT INTO lessons(title, subject_id) VALUES ('Databases lesson 2', %s)"
cursor.execute(lesson4, (subject2_id,))
lesson4_id = cursor.lastrowid
print(lesson4_id)

# Выставляем оценки
mark1 = "INSERT INTO marks(value, lesson_id, student_id) VALUES(10, %s, %s)"
cursor.execute(mark1, (lesson1_id, student_id))

mark2 = "INSERT INTO marks(value, lesson_id, student_id) VALUES(9, %s, %s)"
cursor.execute(mark1, (lesson2_id, student_id))

mark3 = "INSERT INTO marks(value, lesson_id, student_id) VALUES(8, %s, %s)"
cursor.execute(mark1, (lesson3_id, student_id))

mark4 = "INSERT INTO marks(value, lesson_id, student_id) VALUES(7, %s, %s)"
cursor.execute(mark1, (lesson4_id, student_id))

# Выводим все оценки
all_marks = "SELECT * FROM marks WHERE student_id = %s"
cursor.execute(all_marks, (student_id,))
data_marks = cursor.fetchall()
print(data_marks)

# Все книги, которые находятся у студента
all_books = "SELECT title FROM books WHERE taken_by_student_id = %s"
cursor.execute(all_books, (student_id,))
data_books = cursor.fetchall()
print(data_books)

#  Выводим полную информацию о студенте
all_info = """
SELECT students.name AS student,
       `groups`.title AS group_name,
       books.title AS book,
       marks.value AS mark,
       subjets.title AS subject,
       lessons.title AS lesson
FROM students
JOIN `groups` ON `groups`.id = students.group_id
JOIN books ON books.taken_by_student_id = students.id
JOIN marks ON marks.student_id = students.id
JOIN lessons ON lessons.id = marks.lesson_id
JOIN subjets ON subjets.id = lessons.subject_id
WHERE students.id = %s AND `groups`.id = %s;
"""
cursor.execute(all_info, (student_id, group_id))

data_all_info = cursor.fetchall()
print(data_all_info)

print('Выведем таблицу в удобном виде')
print('=' * 167)

for data in data_all_info:
    print(data)

db.commit()
db.close()

print('=' * 167)

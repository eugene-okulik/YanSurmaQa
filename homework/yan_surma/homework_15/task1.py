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
name = 'YanTest'
second_name = 'SurmaTest'

create_student = cursor.execute(
    f"INSERT INTO students(name,second_name, group_id) VALUES ('{name}', '{second_name}', 1)")
student_id = cursor.lastrowid
print(f'id студента {student_id}')

# Создаем книги
create_book1 = cursor.execute(
    f"INSERT INTO books(title,taken_by_student_id) VALUES('SQL and Python. Tom 1', {student_id})")

create_book2 = cursor.execute(
    f"INSERT INTO books(title,taken_by_student_id) VALUES('SQL and Python. Tom 2', {student_id})")

# Создаем группу
create_group = cursor.execute(
    "INSERT INTO `groups`(title, start_date, end_date) VALUES('Video course', 'feb 2024', 'jun 2024');")
group_id = cursor.lastrowid
print(f'id группы {group_id}')

# Обновляем student_id, удобно через переменные
update_student_group_id = cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE students.name = '{name}'")

# Убедимся в обновлении данных о студенте
check_student = cursor.execute(f"SELECT name FROM students WHERE group_id = {group_id}")
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
lesson1 = cursor.execute(f"INSERT INTO lessons(title, subject_id) VALUES ('Python lesson 1', {subject1_id})")
lesson1_id = cursor.lastrowid
print(lesson1_id)

lesson2 = cursor.execute(f"INSERT INTO lessons(title, subject_id) VALUES ('Python lesson 2', {subject1_id})")
lesson2_id = cursor.lastrowid
print(lesson2_id)

lesson3 = cursor.execute(f"INSERT INTO lessons(title, subject_id) VALUES ('Databases lesson 1', {subject2_id})")
lesson3_id = cursor.lastrowid
print(lesson3_id)

lesson4 = cursor.execute(f"INSERT INTO lessons(title, subject_id) VALUES ('Databases lesson 2', {subject2_id})")
lesson4_id = cursor.lastrowid
print(lesson4_id)

# Выставляем оценки
mark1 = cursor.execute(f"INSERT INTO marks(value, lesson_id, student_id) VALUES(10, {lesson1_id}, {student_id})")
mark2 = cursor.execute(f"INSERT INTO marks(value, lesson_id, student_id) VALUES(9, {lesson2_id}, {student_id})")
mark3 = cursor.execute(f"INSERT INTO marks(value, lesson_id, student_id) VALUES(8, {lesson3_id}, {student_id})")
mark4 = cursor.execute(f"INSERT INTO marks(value, lesson_id, student_id) VALUES(7, {lesson4_id}, {student_id})")

# Выводим все оценки
all_marks = cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
data_marks = cursor.fetchall()
print(data_marks)

# Все книги, которые находятся у студента
all_books = cursor.execute(f"SELECT title FROM books WHERE taken_by_student_id = {student_id}")
data_books = cursor.fetchall()
print(data_books)

#  Выводим полную информацию о студенте
all_info = cursor.execute(f"""
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
WHERE students.id = {student_id} AND `groups`.id = {group_id};
""")

data_all_info = cursor.fetchall()
print(data_all_info)

print('Выведем данныые в более удобном виде: ')
for data in data_all_info:
    print(data)


db.commit()
db.close()

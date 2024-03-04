INSERT INTO students(name,second_name, group_id) VALUES('Yan', 'Surma', 1);

SELECT id FROM students WHERE name = 'Yan';
/* 339 */

INSERT INTO books(title,taken_by_student_id) VALUES('Easy SQL', 339);

INSERT INTO books(title,taken_by_student_id) VALUES('Python test automation', 339);

INSERT INTO `groups`(title, start_date, end_date) VALUES('Video course group', 'feb 2024', 'jun 2024');

SELECT id FROM  `groups` WHERE title = 'Video course group';
/* 335 */

UPDATE students SET group_id = 335 WHERE students.name = 'Yan';

INSERT INTO subjets(title) VALUES ('Programming in Python');
SELECT id FROM subjets WHERE title = 'Programming in Python'; 
/* 426 */
INSERT INTO subjets(title) VALUES ('DATABASE with SQL');
SELECT id FROM subjets WHERE title = 'DATABASE with SQL'; 
/* 427 */
INSERT INTO lessons(title, subject_id) VALUES ('py1', 426);
INSERT INTO lessons(title, subject_id) VALUES ('py2', 426);
INSERT INTO lessons(title, subject_id) VALUES ('db1', 427);
INSERT INTO lessons(title, subject_id) VALUES ('db2', 427);

SELECT id FROM lessons WHERE title = 'py1' AND subject_id = 426;
/* 411 */
SELECT id FROM lessons WHERE title = 'py2' AND subject_id = 426;
/* 412 */
SELECT id FROM lessons WHERE title = 'db1' AND subject_id = 427;
/* 413 */
SELECT id FROM lessons WHERE title = 'db2' AND subject_id = 427;
/* 414 */

INSERT INTO marks(value, lesson_id, student_id) VALUES(10, 411, 339);
INSERT INTO marks(value, lesson_id, student_id) VALUES(9, 412, 339);
INSERT INTO marks(value, lesson_id, student_id) VALUES(8, 413, 339);
INSERT INTO marks(value, lesson_id, student_id) VALUES(7, 414, 339);

/* Все оценки студента */
SELECT * FROM marks WHERE student_id = 339;

/* Все книги, которые находятся у студента */
SELECT title FROM books
WHERE taken_by_student_id = 339;

/* Группа, книги, оценки, назв. занятия, назв. предмета */
SELECT students.name AS student_name,
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
WHERE students.id = 339 AND `groups`.id = 335;
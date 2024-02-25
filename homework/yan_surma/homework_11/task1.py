class Book:
    material = 'бумага'
    text_exists = True
    isbn = 'ISBN 978-5-699-12014-7'  # Пусть будет общим для всех
    reserved = False

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def book_details(self):
        if self.reserved:
            return (f'Название: {self.name}, '
                    f'Автор: {self.author}, '
                    f'страниц: {self.pages}, '
                    f'материал: {self.material}, '
                    f'зарезервирована')
        else:
            return (f'Название: {self.name}, '
                    f'Автор: {self.author}, '
                    f'страниц: {self.pages}, '
                    f'материал: {self.material}')


book1 = Book('Война и мир', 'Толстой', 1225)
book2 = Book('Преступление и наказание', 'Достоевский', 671)
book3 = Book('Анна Каренина', 'Толстой', 864)
book4 = Book('Братья Карамазовы', 'Достоевский', 796)
book5 = Book('Мастер и Маргарита', 'Булгаков', 384)

print(book1.book_details())
book1.reserved = True
print(book1.book_details())


class SchoolBook(Book):
    have_tasks = True

    def __init__(self, name, author, pages, subject, class_number):
        super().__init__(name, author, pages)
        self.subject = subject
        self.class_number = class_number

    def book_details(self):
        if self.reserved:
            return (f'Название: {self.name}, '
                    f'Автор: {self.author}, '
                    f'страниц: {self.pages}, '
                    f'предмет: {self.subject}, '
                    f'класс: {self.class_number}, '
                    f'зарезервирована')
        else:
            return (f'Название: {self.name}, '
                    f'Автор: {self.author}, '
                    f'страниц: {self.pages}, '
                    f'предмет: {self.subject}, '
                    f'класс: {self.class_number}')


school_book1 = SchoolBook('Алгебра', 'Петров', 300, 'Математика', 9)
school_book2 = SchoolBook('Геометрия', 'Сидоров', 250, 'Математика', 9)
school_book3 = SchoolBook('Тригонометрия', 'Васильев', 350, 'Математика', 9)

print(school_book3.book_details())
school_book3.reserved = True
print(school_book3.book_details())

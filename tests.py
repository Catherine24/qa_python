from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_cant_add_book_twice_same_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 2

    def test_set_book_rating_cant_add_rating_book_new_book_none(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_rating('Палата номер шесть', 6)

        assert collector.get_book_rating('Палата номер шесть') == None

    def test_get_book_rating_book_exist_six(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_rating('Гордость и предубеждение и зомби', 6)

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 6


    def test_get_books_with_specific_rating_spesific_rating_six(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')


        assert collector.get_books_with_specific_rating(1) == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']



    def test_get_books_rating_all_books_one(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert collector.get_books_rating() == {'Гордость и предубеждение и зомби': 1, 'Что делать, если ваш кот хочет вас убить': 1}

    def test_add_book_in_favorites_one(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')


        collector.add_book_in_favorites('Гордость и предубеждение и зомби')


        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites_one(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []


    def test_get_list_of_favorites_books_one_book(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби','Что делать, если ваш кот хочет вас убить']


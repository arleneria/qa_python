import pytest

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
    def test_set_book_rating_rating5_add_rating(self):
        collector = BooksCollector()
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.set_book_rating(book, 5)
        assert collector.get_book_rating(book) == 5

    def test_get_book_rating_unadded_book_shows_error(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Гордость и предубеждение') in range (1, 11), 'This book is not added'


    def test_get_books_with_specific_rating_rating3_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Трое в лодке: нищета и собаки')
        collector.add_new_book('Анна Корнеева')
        collector.add_new_book('Убить переснежника')
        collector.set_book_rating('Трое в лодке: нищета и собаки', 3)
        collector.set_book_rating('Анна Корнеева', 6)
        collector.set_book_rating('Убить переснежника', 3)
        assert len(collector.get_books_with_specific_rating(3)) == 2

    def test_get_books_rating_one_book_get_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Трое в лодке: нищета и собаки')
        assert collector.get_books_rating() == {'Трое в лодке: нищета и собаки': 1}

    def test_add_book_in_favorites_one_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Кря')
        collector.add_book_in_favorites('Кря')
        assert collector.get_list_of_favorites_books() == ['Кря']

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Над пропостью в траве')
        collector.add_new_book('Обломкин')
        collector.add_book_in_favorites('Над пропостью в траве')
        collector.add_book_in_favorites('Обломкин')
        collector.delete_book_from_favorites('Обломкин')
        assert collector.get_list_of_favorites_books() == ['Над пропостью в траве']

    def test_get_list_of_favorites_books_one_book_get_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Мяу')
        collector.add_book_in_favorites('Мяу')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_unadded_book_shows_error(self):
        collector = BooksCollector()
        assert collector.delete_book_from_favorites('Кря'), 'Cannot delete unadded book'

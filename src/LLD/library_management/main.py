import datetime
import uuid
from abc import ABC
from constants import *


class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []


class Account:
    def __init__(self, username, password, person, status=AccountStatus.ACTIVE):
        self.username = username
        self._password = password
        self.status = status
        self.account_id = uuid.uuid1()
        self.person = person

    def change_password(self, password):
        if self._password == password:
            return
        self._password = password


class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode


class Rack:
    def __init__(self, number, location_identifier):
        self.number = number
        self.location_identifier = location_identifier


class Book(ABC):
    def __init__(self, title, subject, publisher, language, number_of_pages):
        self.unique_id = uuid.uuid4()
        self.title = title
        self.subject = subject
        self.publisher = publisher
        self.language = language
        self.number_of_pages = number_of_pages
        self.authors = []

    def add_authors(self, author):
        self.authors.append(author)


class BookItem(Book):
    def __init__(
            self, title, subject, publisher, language, number_of_pages, bar_code, publication_date,
            book_status=BookStatus.AVAILABLE, book_format=BookFormat.HARDCOVER, rack=None
    ):
        super().__init__(title, subject, publisher, language, number_of_pages)
        self.bar_code = bar_code
        self.publication_date = publication_date
        self.book_status = book_status
        self.book_format = book_format
        self.rack = rack


class Person(ABC):
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone


class Author(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


class Member(Account):
    def __init__(self, first_name, last_name, email, phone):
        super().__init__(first_name, last_name, email, phone)
        self.date_of_membership = datetime.datetime.today()
        self._total_books_checked_out = 0

    def reserve_book_item(self, book_item):
        pass

    def increment_books_checked_out(self):
        self._total_books_checked_out += 1

    def renew_book_item(self, book_item):
        pass

    def check_for_fine(self, book_item):
        pass

    def return_book_item(self, book_item):
        pass

    def renew_book_item(self, book_item):
        pass


class Librarian(Account):
    def __init__(self, account_id, password, status=AccountStatus.ACTIVE):
        super().__init__(account_id, password, status)

    def add_book_item(self, book: BookItem):
        pass

    def block_member(self, user):
        pass

    def unblock_member(self, user):
        pass


class SearchBook(ABC):

    def search_book_by_title(self, title):
        pass

    def search_book_by_publication_date(self, publication_date):
        pass

    def search_book_by_author(self, author_name):
        pass

    def search_book_by_book_type(self, book_type):
        pass


class Catalog(SearchBook):
    def __init__(self):
        self._book_titles = {}
        self._book_authors = {}
        self._book_subjects = {}
        self._book_publication_dates = {}

    def search_by_title(self, query):
        return self._book_titles.get(query)

    def search_by_author(self, query):
        return self._book_authors.get(query)


class BookLending:
    def __init__(self, book, user):
        self.book = book
        self.start_date = datetime.datetime.today()
        self.due_date = self.start_date + datetime.timedelta(days=DUE_IN_DAYS)
        self.user = user

    def get_return_date(self):
        return self.due_date


class BookReservation:
    def __init__(self):
        self._creation_date = None
        self._status = None
        self._book_item_barcode = None
        self._member_id = None

    def check_for_fine(self, creation_date, status, book_item_barcode, member_id):
        self._creation_date = creation_date
        self._status = status
        self._book_item_barcode = book_item_barcode
        self._member_id = member_id

    def fetch_reservation_details(self, barcode):
        return


class Fine:
    def __init__(self):
        self._creation_date = None
        self._book_item_barcode = None
        self._member_id = None
        self.charges = 0

    def check_for_fine(self, creation_date, book_item_barcode, member_id):
        self._creation_date = creation_date
        self._book_item_barcode = book_item_barcode
        self._member_id = member_id

    def get_charges(self, days):
        self.charges = FINE_PER_DAY * days
        return self.charges


def main():
    ...


if __name__ == '__main__':
    main()

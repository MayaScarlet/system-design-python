import datetime
import uuid
from constants import *
from abc import ABC
from collections import defaultdict


class BookMyShow:
    def __init__(self):
        self._cinemas = defaultdict(list)  # key: city, values: cinemas
        self._cities = []
        self._movies = []

    def get_movies(self):
        """ Displays all movies on the platform irrespective of city/cinema hall"""
        return self._movies

    def get_cities(self):
        """ Returns a list of cities where affiliate cinemas are located """
        return self._cities

    def get_cinema(self, city):
        """ Returns a list of cinema halls or multiplexes affiliated to selected city """
        return self._cinemas[city]


class Cinema:
    def __init__(self, cinema_id, name, address):
        self.id = cinema_id
        self.name = name
        self.address = address
        self.screens = []

    def get_movies(self):
        """ Returns a list of movies per selected cinema """
        return

    def get_screens_count(self):
        """Returns no of screens in a cinema"""
        return len(self.screens)


class Screen:
    def __init__(self, screen_id, title, total_seats):
        self.id = screen_id
        self.title = title
        self.total_seats = total_seats
        self._shows = []


class Show:
    def __init__(self, show_id, movie, start_time, end_time):
        self.show_id = show_id
        self.movie = movie
        self.start_time = start_time
        self.end_time = end_time
        self.cinema_played_at = []
        self.seats = []


class Seat:
    def __init__(self, seat_id, seat_type=SeatType.REGULAR, status=SeatStatus.AVAILABLE):
        self.id = seat_id
        self.type = seat_type
        self.status = status
        self.cost = SeatCharges.REGULAR
        self.row = 0
        self.column = 0

    def __repr__(self):
        return f"{self.row} {self.column}"

    def get_cost(self):
        return self.cost


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class User:
    def __init__(self, name, email, address, username, password):
        self.name = name
        self.email = email
        self.address = address
        self.account = Account(username, password)


class Guest(User):
    def __init__(self, name, email, address, username, password):
        super().__init__(name, email, address, username, password)
        self._bookings = []

    def register_account(self):
        return

    def change_password(self):
        return

    def view_past_bookings(self):
        """Returns a list of past bookings"""
        return self._bookings

    def confirm_booking(self, booking_id):
        """State where user has selected show and seats but not checked out"""
        return


class FrontDeskOfficer(Account):
    def __init__(self, username, password):
        super().__init__(username, password)

    def create_booking(self, movie):
        return


class Admin(Account):
    def __init__(self, username, password):
        super().__init__(username, password)

    def add_movies(self):
        return

    def modify_movie(self, movie):
        return

    def add_shows(self, show):
        return

    def modify_shows(self, show):
        return


class Movie:
    def __init__(self, movie_id, name, description, runtime):
        self.movie_id = movie_id
        self.name = name
        self.description = description
        self.runtime = runtime
        self.formats = []
        self.languages = []
        self.genres = []
        self.release_date = None
        self._shows = []

    def add_languages(self, language):
        return self.languages.append(language)

    def add_genre(self, genre):
        return self.genres.append(genre)

    def get_movie_shows(self):
        return self._shows

    def create_booking(self):
        """
            User -> Movie -> Book tickets -> Select language and format -> Select Show -> Select no of seats -> Checkout
        """
        return


class City:
    def __init__(self, name, zipcode):
        self.name = name
        self.zipcode = zipcode


class Booking:
    def __init__(self, movie, status=BookingStatus.PROGRESS):
        self.id = uuid.uuid4()
        self.booking_date = datetime.datetime.today()
        self.movie = movie
        self.status = status
        self.show = None
        self.no_of_seats = 1
        self.charges = 0
        self.language = None
        self.format = None
        self.seats = []
        self.payment_status = None
        self.amount = 0

    def select_language(self, language: str):
        self.language = language

    def select_format(self, movie_format: str):
        self.format = movie_format

    def select_show(self, show, no_of_seats):
        self.show = show
        self.no_of_seats = no_of_seats

    def select_seats(self, seat_type: str, row: int, column: int):
        """Seats in the format of row[A-Z] and column [1-23]"""
        seat = Seat(seat_type, row, column)
        self.amount += seat.cost
        self.seats.append(seat)

    def checkout(self):
        """
        Checkout -> Payment -> Transaction -> Add Coupon[if any] -> Add Discount[if any] -> Pay -> Booking Confirmed
        """
        transaction = Transaction()
        transaction.add_coupon()
        self.amount = transaction.get_total_charges(self.amount)
        self.payment_status = PaymentStatus.CONFIRMED
        self.status = BookingStatus.CONFIRMED

    def get_booking_details(self):
        """Returns booking details for a booking id"""
        json = {
            'movie': self.movie,
            'show': self.show,
            'seats': self.seats,
            'language': self.language,
            'format': self.format,
        }
        return json

    def cancel(self):
        return


class Search(ABC):
    def search_movie_by_title(self, title):
        return

    def search_movie_by_language(self, language):
        return

    def search_movie_by_genre(self, genre):
        return

    def search_by_release_date(self, date):
        return

    def search_by_city(self, city):
        return

    def search_by_movie_format(self, movie_format):
        return


class Catalog(Search):
    def __init__(self):
        self.last_updated = datetime.datetime.today()
        self.movie_titles = dict()
        self.movie_languages = dict()
        self.movie_genres = dict()
        self.movie_cities = dict()
        self.movie_releases = dict()
        self.movie_formats = dict()

    def search_movie_by_title(self, query):
        return self.movie_titles[query]

    def search_by_release_date(self, date):
        return self.movie_releases[date]

    def search_movie_by_genre(self, genre):
        return self.movie_genres[genre]

    def search_movie_by_language(self, language):
        return self.movie_languages[language]

    def search_by_city(self, city):
        return self.movie_languages[city]

    def search_movie_by_format(self, movie_format):
        return self.movie_formats[movie_format]


class Transaction:
    def __init__(self):
        self.transaction_id = uuid.uuid4()
        self.total_charges = None
        self.payment_method = None
        self.gateway_charges = None
        self.coupon = None   # Some gateway methods or payment platforms give coupon codes
        self.discount = None   # There can be seasonal discounts on certain movies

    def add_coupon(self, code=None):
        if code:
            self.coupon = code

    def get_total_charges(self, amount_to_pay):
        amount = amount_to_pay + self.calculate_gateway_charges(self.gateway_charges)
        if self.discount is not None:
            total_discount = self.discount.get_discount(amount_to_pay)
            amount -= total_discount

        if self.coupon is not None:
            coupon_discount = self.coupon.fetch_coupon_discount(amount_to_pay)
            amount -= coupon_discount
        return amount

    def calculate_gateway_charges(self, selected_gateway):
        """Some gateway have fixed charges while some charge in percent"""
        return


class Coupon:
    def __init__(self, coupon_code, coupon_type=CouponType.FIXED, cost=0):
        self.coupon_code = coupon_code
        self.coupon_type = coupon_type
        self.cost = cost

    def fetch_coupon_discount(self, amount_to_pay):
        if self.coupon_type == "FIXED":
            return self.cost
        return amount_to_pay - float(self.cost/100 * amount_to_pay)


class Discount:
    def __init__(self, name, discount_type=CouponType.FIXED, cost=0):
        self.name = name
        self.discount_type = discount_type
        self.cost = cost

    def get_discount(self, amount_to_pay):
        if self.discount_type == "FIXED":
            return self.cost
        return amount_to_pay - float(self.cost/100 * amount_to_pay)


def main():
    ...


if __name__ == '__main__':
    main()

from enum import Enum


FINE_PER_DAY = 10
MAX_BOOKS_LIMIT = 5
FINE_PER_LOST_BOOK = 500
DUE_IN_DAYS = 15


class ReservationStatus(Enum):
    CONFIRMED = 1
    CANCELLED = 2
    WAITING = 3


class BookStatus(Enum):
    AVAILABLE = 1
    LOANED = 2
    RESERVED = 3
    LOST = 4


class BookFormat(Enum):
    HARDCOVER = 1
    PAPERBACK = 2
    NEWSPAPER = 3
    PUBLICATION = 4
    MAGAZINE = 5
    AUDIOBOOK = 6
    EBOOK = 7


class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    BLOCKED = 3
    CANCELLED = 4

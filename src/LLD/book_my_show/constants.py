from enum import Enum


class BookingStatus(Enum):
    PROGRESS = "PROGRESS"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    RESERVED = "RESERVED"
    PENDING = "PENDING"


class PaymentStatus(Enum):
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    PENDING = "PENDING"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
    UNPAID = "UNPAID"


class SeatType(Enum):
    REGULAR = "REGULAR"
    CLASSIC = "CLASSIC"
    PREMIUM = "PREMIUM"
    VIP = "VIP"


class SeatStatus(Enum):
    AVAILABLE = "AVAILABLE"
    OCCUPIED = "OCCUPIED"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    RESERVED = "RESERVED"


class CouponType(Enum):
    PERCENT = "PERCENT"
    FIXED = "FIXED"


class Genre(Enum):
    SCI_FI = "SCI_FI"
    ROMANCE = "ROMANCE"
    ROM_COM = "ROM_COM"
    FANTASY = "FANTASY"
    ACTION = "ACTION"
    THRILLER = "THRILLER"
    DRAMA = "DRAMA"
    ADVENTURE = "ADVENTURE"


class MovieFormat(Enum):
    IMAX_3D = "IMAX_3D"
    SCREEN_X = "3D_SCREEN_X"
    THREE_D = "3D"
    TWO_D = "2D"


class SeatCharges:
    REGULAR = 200
    CLASSIC = 350
    PREMIUM = 500
    VIP = 1000

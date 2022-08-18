from enum import Enum, auto


class BookingStatus(Enum):
	CONFIRMED = auto()
	CANCELLED = auto()
	PENDING = auto()


class PaymentStatus(Enum):
	SUCCESS = auto()
	FAILED = auto()
	REJECTED = auto()
	CANCELLED = auto()
	PENDING = auto()


class FlightClass(Enum):
	ECONOMY = auto()
	PREMIUM_ECONOMY = auto()
	BUSINESS = auto()
	FIRST_CLASS = auto()


class FlightStatus(Enum):
	ACTIVE = auto()
	SCHEDULED = auto()
	ARRIVED = auto()
	DELAYED = auto()
	DEPARTED = auto()
	DIVERTED = auto()
	CANCELLED = auto()
	IN_AIR = auto()


class BookingType(Enum):
	ONE_WAY = auto()
	ROUND_TRIP = auto()


class CheckInStatus(Enum):
	CHECKED_IN = auto()

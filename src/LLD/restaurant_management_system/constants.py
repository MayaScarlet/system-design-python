from enum import Enum, auto


class AccountStatus(Enum):
	ACTIVE = auto()
	DEACTIVATED = auto()
	DELETED = auto()
	BLACKLISTED = auto()


class PaymentStatus(Enum):
	SUCCESS = auto()
	REJECTED = auto()
	PENDING = auto()
	CANCELLED = auto()


class ReservationStatus(Enum):
	REQUESTED = auto()
	PENDING = auto()
	CONFIRMED = auto()
	CHECKED_IN = auto()
	CANCELLED = auto()


class TableStatus(Enum):
	AVAILABLE = auto()
	RESERVED = auto()
	OCCUPIED = auto()


class OrderStatus(Enum):
	RECIEVED = auto()
	PREPARING = auto()
	COMPLETED = auto()
	CANCELLED = auto()


class PaymentMode(Enum):
	CREDIT_CARD = auto()
	CASH = auto()
	CHEQUE = auto()

from enum import Enum, auto


class ConnectionInvitationStatus(Enum):
	PENDING = auto()
	ACCEPTED = auto()
	CONFIRMED = auto()
	REJECTED = auto()
	CANCELED = auto()


class AccountStatus(Enum):
	ACTIVE = auto()
	BLOCKED = auto()
	BANNED = auto()
	COMPROMISED = auto()
	ARCHIVED = auto()
	UNKNOWN = auto()


class OrganizationType(Enum):
	PUBLIC_COMPANY = auto()
	SELF_EMPLOYED = auto()
	GOVERNMENT_AGENCY = auto()
	NON_PROFIT = auto()
	PRIVATE = auto()
	PARTNERSHIP = auto()


class EmploymentType(Enum):
	FULL_TIME = auto()
	PART_TIME = auto()
	TRAINEE = auto()
	FREELANCE = auto()
	INTERNSHIP = auto()
	SELF_EMPLOYED = auto()


class InvitationStatus(Enum):
	SUCCESS = auto()
	PENDING = auto()
	CANCELLED = auto()
	REJECTED = auto()

from dataclasses import dataclass, field
from typing import List

from constants import AccountStatus
from main import Reservation

@dataclass
class Account:
	username: str
	email: str
	password: str
	account_status: AccountStatus
	name: str
	phone: str
	address: str

	def reset_password(self):
		...


@dataclass
class Employee(Account):
	employee_id: int
	date_joined: str

	def __post_init__(self):
		super().__init__(self)

	def place_order(self):
		...

	def view_order(self):
		...


@dataclass
class Receptionist(Employee):

	def __post_init__(self):
		super().__init__(self)

	def create_reservation(self):
		...

	def search(self):
		...


@dataclass
class Manager(Employee):

	def __post_init__(self):
		super().__init__(self)

	def add_employee(self):
		...


@dataclass
class Waiter(Employee):

	def __post_init__(self):
		super().__init__(self)

	def create_order(self):
		...


@dataclass
class Chef(Employee):

	def __post_init__(self):
		super().__init__(self)

	def take_order(self):
		...


@dataclass
class Customer(Account):
	reservations: List[Reservation] = field(default_factory=list, repr=False)

	def __post_init__(self):
		super().__init__(self)

	def create_reservation(self):
		...

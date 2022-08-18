from dataclasses import dataclass, field

from typing import List

from constants import OrderStatus, TableStatus, ReservationStatus, PaymentMode
from user import Customer, Waiter
import datetime
import uuid


@dataclass
class Kitchen:
	name: str
	chefs: list = field(default_factory=list, repr=False)

	def assign_chef(self, chef):
		...


@dataclass
class Reservation:
	people_count: int
	checkin_date: str
	checkin_time: str
	customer: Customer = None
	status: ReservationStatus = ReservationStatus.REQUESTED
	created_at: str = datetime.datetime.now()
	reservation_id: str = uuid.uuid4()
	notifications: list = None

	def update_people(self, count):
		...

	def cancel_reservation(self):
		...


@dataclass
class Restaurent:
	name: str
	branches: list = field(default_factory=list, repr=False)

	def add_branch(self):
		...


@dataclass
class MenuItem:
	item_id: str
	title: str
	price: float
	description: str = None

	def update_info(self, title: str, desc: str):
		...

	def update_price(self, price: float):
		...


@dataclass
class MenuSection:
	section_id: int
	menu_items: List[MenuItem] = field(default_factory=dict, repr=True)

	def add_menu_item(self, menu_item):
		...

	def remove_menu_item(self, menu_item):
		...


@dataclass
class Menu:
	menu_id: int
	title: str
	description: str
	menu_sections: List[MenuSection] = field(default_factory=list, repr=False)

	def add_menu_section(self, section):
		...

	def print(self):
		...


@dataclass
class Seat:
	seat_id: int


@dataclass
class Table:
	capacity: int
	table_status: TableStatus = TableStatus.AVAILABLE
	seats: List[Seat] = field(default_factory=list, repr=False)

	def update_seats(self):
		...


@dataclass
class MealItem:
	meal_item_id: int
	servings: int
	menu_item: MenuItem

	def update_servings(self):
		...


@dataclass
class Meal:
	meal_id: int
	meal_items: List[MealItem]
	servings: int
	seat: Seat

	def add_meal_item(self):
		...

	def remove_meal_item(self):
		...


@dataclass
class Order:
	order_id: int
	meals: List[Meal]
	table: Table
	waiter: Waiter
	created_at = datetime.datetime.today()
	order_status: OrderStatus = None

	def get_status(self):
		...




@dataclass
class Bill:
	bill_id: int
	table: Table
	waiter: Waiter
	amount_to_pay: float
	bill_items: dict = field(default_factory=dict, repr=False)


@dataclass
class Payment:
	bill: Bill
	amount_paid: float
	customer: Customer
	mode_of_payment: PaymentMode
	payment_id: str = uuid.uuid1()

	def print_receipt(self):
		...

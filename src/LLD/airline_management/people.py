from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from main import FlightBooking


@dataclass
class Account:
	name: str
	username: str
	email: str
	phone: str
	address: str
	password: str

	def logout(self):
		...

	def reset_password(self):
		...


@dataclass
class User(Account):
	bookings: List[FlightBooking] = field(default_factory=list, repr=False)

	def create_booking(self):
		...


@dataclass
class Admin(Account):
	def add_aircraft(self):
		...

	def add_flight_schedule(self, flight_schedule):
		...

	def cancel_flight(self, flight):
		...

	def update_flight(self, flight):
		...

	def update_flight_schedule(self, flight_schedule):
		...


@dataclass
class Crew(Account):
	def get_flights(self):
		...


@dataclass
class Pilot(Account):
	def get_flights(self):
		...


@dataclass
class FrontDeskOfficer(Account):

	def check_in(self, passenger):
		...

	def check_bookings(self):
		...

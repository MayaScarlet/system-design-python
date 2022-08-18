from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import List
from constants import (
	BookingStatus, FlightClass, FlightStatus, CheckInStatus, BookingType
)


@dataclass
class Aircraft:
	aircraft_id: int  # ICAO 24 bit address
	aircraft_type: str
	registration: str
	country_of_registration: str
	manufacturing_year: int
	seats: List[FlightSeat] = field(default_factory=list, repr=False)


@dataclass
class FlightSeat:
	flight_class: FlightClass
	seat_number: int | str


@dataclass
class Airline:
	name: str
	airline_code: str
	country_code: str
	fleet: int
	aircrafts: List[Aircraft] = field(default_factory=list, repr=False)
	registration: str = None
	routes: defaultdict[List] = field(default_factory=list, repr=False)

	def update_routes(self):
		...

	def update_aircraft(self, aircraft):
		...


@dataclass
class Airport:
	name: str
	location: str
	airport_code: str
	location_iso_code: str
	elevation_level: str
	timezone: str
	affiliated_airlines: List[Airline] = field(default_factory=list, repr=True)

	def update_airline(self):
		...


@dataclass
class Flight:
	flight_no: str | int
	aircraft: Aircraft
	arrival_airport: Airport
	departure_airport: Airport
	schedules: List[FlightSchedule] = field(default_factory=list)


@dataclass
class FlightSchedule:
	scheduled_arrival: float
	scheduled_departure: float
	actual: float
	estimated: float
	ground_speed: int
	calibrated_altitude: int
	status: FlightStatus

	def update_arrival_time(self):
		...

	def update_departure_time(self):
		...


@dataclass
class FlightBooking:
	booking_id: int
	flight_schedule: FlightSchedule
	extra_services: list
	amount: float
	booking_type: BookingType
	extra_services: dict = field(default_factory=dict, repr=False)
	passengers: List[Passenger] = field(default_factory=list)
	tickets: List[FlightTicket] = field(default_factory=list, repr=False)
	booking_status: BookingStatus = None

	def add_extra_services(self):
		...

	def get_passengers(self):
		...

	def cancel(self):
		...


@dataclass
class Passenger:
	name: str
	address: str
	gender: str
	age: int
	identification_id: str


@dataclass
class FlightTicket:
	ticket_no: str | int
	schedule: FlightSchedule
	passenger: Passenger
	seat: FlightSeat

	def upgrade(self):
		...


@dataclass
class CheckIn:
	checkin_id: int
	passenger: Passenger
	check_in_status: CheckInStatus

	def set_status(self, status):
		...


def main():
	...


if __name__ == '__main__':
	main()

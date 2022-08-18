from abc import ABC
from .constants import *
import uuid


class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

    def __repr__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"


class Hotel:
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms

    def room_count(self):
        return self.rooms

    def __str__(self):
        return f"Hotel: {self.name}"


class Person(ABC):
    def __init__(self, name: str, address, email: str, phone: str, account_type: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.account_type = account_type


class Guest(Person):
    def __init__(self, name, address, email, phone):
        super(Person, self).__init__(name, address, email, phone, AccountType.GUEST)
        self._bookings = []
        
    def search_room(self):
        return

    def book_room(self):
        return


class HouseKeeper(Person):
    def __init__(self, name, address, email, phone):
        super(Person, self).__init__(name, address, email, phone, AccountType.HOUSEKEEPER)

    def add_log(self, room_id):
        ...


class Admin(Person):
    def __init__(self, name, address, email, phone):
        super(Person, self).__init__(name, address, email, phone, AccountType.ADMIN)

    def add_room(self):
        return

    def remove_room(self, room_id):
        return

    def assign_housekeeper(self, room_id):
        return

    def assign_rooms(self):
        return


class Booking:
    def __init__(self):
        self.booking_id = uuid.uuid4()
        self.room_type = None
        self.amount = None
        self.check_in_date = None
        self.check_out_date = None
        self.total_amount_paid = None

    def select_rooms(self):
        return

    def select_check_in_date(self):
        return

    def select_check_out_date(self):
        return

    def checkout(self):
        return


class Discount:
    def __init__(self, code, cost, discount_type=DiscountType.FIXED):
        self.discount_code = code
        self.discount_type = discount_type
        self.cost = cost

    def calculate(self):
        return


class Payment:
    def __init__(self, booking_id, amount_payable):
        self.booking_id = booking_id
        self.payment_id = uuid.uuid4()
        self.amount = amount_payable
        self.discount_applied = None
        self.payment_status = None

    def apply_discount(self):
        if self.discount_applied == "FIXED":
            self.amount -= self.discount_applied.cost
        self.amount = self.amount - float(self.amount/100 * self.amount)

    def update_payment_status(self):
        self.payment_status = PaymentStatus.CONFIRMED


def main():
    ...


if __name__ == '__main__':
    main()

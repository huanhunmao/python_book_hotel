import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Ticket(ABC):
    @abstractmethod
    def  generate(self):
        pass

class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(count):
        return count * 7.2


class DigitalTicket(Ticket):
    def generate(self):
        return 'Hello, this is your digital ticket'

    def download(self):
        pass

ticket = Ticket()
# TypeError: Can't instantiate abstract class Ticket with abstract method generate
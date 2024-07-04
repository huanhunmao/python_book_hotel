import pandas as pd

# class User:
#     pass

df = pd.read_csv('hotels.csv', dtype=str)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        df.loc[df['id'] == self.hotel_id ,'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self,customer_name, customer_object):
        pass

    def generate(self):
        pass


# print(df) 拿到整个表
hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = ReservationTicket(name, hotel)
    reservation_ticket.generate()
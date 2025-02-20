import pandas as pd

# class User:
#     pass

df = pd.read_csv('hotels.csv', dtype=str)
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pd.read_csv('card_security.csv', dtype=str)
print(df_cards)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        df.loc[df['id'] == self.hotel_id ,'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class ReservationTicket:
    def __init__(self,customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name:{self.customer_name}
        Hotel name:{self.hotel.name}
        """

        return content


class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here are you SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        have fun!
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {
            'number': self.number,
            'expiration': expiration,
            'holder': holder,
            'cvc': cvc
        }
        if card_data in df_cards:
            return True
        else:
            return False


# 类继承 CreditCard
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number'] == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        else:
            return False

# print(df) 拿到整个表
hotel_id = input('Enter the id of the hotel: ')
hotel = SpaHotel(hotel_id)

if hotel.available():
    card_security_data = SecureCreditCard(number='1234567890123456')
    if card_security_data.validate(expiration='12/28',
                           holder='JANE SMITH', cvc='456'):
        if card_security_data.authenticate(given_password='mypass'):
            hotel.book()
            name = input('Enter your name: ')
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            res = reservation_ticket.generate()
            print(res)
            spa = input('Do u want to book a spa package? ')
            if spa == 'yes':
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())
        else:
            print('SecureCreditCard check failed!')
    else:
        print('Please check your payment!')
else:
    print('Hotel is not free!')
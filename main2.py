import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    common_data = 'This is a common data'
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

class ReservationTicket:
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

hotel1 = Hotel('134')
print(hotel1.name) # Tourist Sunny Apartment

hotel2 = Hotel('188')
print(hotel2.name) # Snow Palace

print(hotel1.common_data) # This is a common data
print(hotel2.common_data) # This is a common data

# 也可以写成
print(Hotel.common_data) # This is a common data

# 类的方法
print(Hotel.get_hotel_count(data=df)) # 3

ticket = ReservationTicket( customer_name=' KK adad ', hotel_object=hotel1)
print(ticket.the_customer_name) # Kk Adad
print(ticket.generate())  # 此处 也能用
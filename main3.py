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

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

# 1、执行 'hello' == 'hi'
print('hello' == 'hi') # False
# 实际执行
print('hello'.__eq__('hi')) # False

# 2、两个实例  是不相同的  即使传入相同 id
hotel1 = Hotel('188')
hotel2 = Hotel('188')
print(hotel1 == hotel2) # False
print(hotel1.__eq__(hotel2)) # NotImplemented

# 3、更改 类的 __eq__ 方法 估计比较少用吧
print(hotel1.__eq__(hotel2)) # True


















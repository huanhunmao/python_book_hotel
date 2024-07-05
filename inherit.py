# 基础继承  && 修改继承方法

class Ticket:
    def __init__(self):
        pass

    def generate(self):
        print('This is your ticket')


class TicketChildren(Ticket):
    def download(self):
        pass

    # 重写了 方法
    def generate(self):
        print('Vip! give u ticket')


tt = TicketChildren()
tt.generate()  # Vip! give u ticket
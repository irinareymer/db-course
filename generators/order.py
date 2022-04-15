import datetime
import random
from faker import Faker


class Order:
    date_of_order: datetime.date
    order_price: int
    status: str

    fake = Faker()

    def __init__(self):
        self.__date_of_order_gen()
        self.__order_price()
        self.__status()

    def __date_of_order_gen(self):
        self.date_of_order = self.fake.date_between_dates(date_start=datetime.date(2005, 1, 1),
                                                          date_end=datetime.date.today())

    def __order_price(self):
        self.order_price = random.randint(10, 10000)

    def __status(self):
        self.status = random.choice(['in progress', 'ready', 'delivered'])

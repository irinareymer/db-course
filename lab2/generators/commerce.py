import datetime
import random
from typing import Optional
from faker import Faker


class Commerce:

    price: int
    availability: str
    arrive: Optional[datetime.date]

    fake = Faker()

    def __init__(self):
        self.__price_gen()
        self.__availability_gen()
        self.__arrive_gen()

    def __price_gen(self):
        self.price = random.randint(500, 10000)

    def __availability_gen(self):
        self.availability = random.choice(['in stock', 'out of stock', 'no longer produced'])

    def __arrive_gen(self):
        if self.availability == 'out of stock':
            self.arrive = self.fake.future_date()
        else:
            self.arrive = None

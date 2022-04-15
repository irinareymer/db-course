import datetime
import random
from faker import Faker


class Sale:
    name: str
    discount: int
    start: datetime.date
    finish: datetime.date

    fake = Faker()

    def __init__(self):
        self.__name_gen()
        self.__discount_gen()
        self.__start_gen()
        self.__finish_gen()

    def __name_gen(self):
        self.name = self.fake.word()

    def __discount_gen(self):
        self.discount = random.randint(1, 100)

    def __start_gen(self):
        self.start = self.fake.date_between_dates(date_start=datetime.date(2005, 1, 1),
                                                  date_end=datetime.date.today())

    def __finish_gen(self):
        self.finish = self.fake.date_between_dates(date_start=self.start + datetime.timedelta(days=1),
                                                   date_end=self.fake.future_date())

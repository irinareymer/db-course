import datetime
from typing import Optional
from faker import Faker


class Feedback:

    review: Optional[str]
    questions: Optional[str]
    date_of_publication: datetime.date

    fake = Faker()

    def __init__(self):
        self.__review_gen()
        self.__question_gen()
        self.__date_of_publication_gen()

    def __review_gen(self):
        gen = self.fake.boolean()
        if gen:
            self.review = self.fake.text()
        else:
            self.review = None

    def __question_gen(self):
        gen = self.fake.boolean()
        if gen:
            self.questions = self.fake.text()
        else:
            self.questions = None

    def __date_of_publication_gen(self):
        self.date_of_publication = self.fake.date_between_dates(date_start=datetime.date(2005, 1, 1),
                                                                date_end=datetime.date.today())

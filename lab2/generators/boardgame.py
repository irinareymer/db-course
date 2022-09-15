import datetime
from typing import Optional
from faker import Faker
import random
from uuid import uuid4


class BoardGame:
    name: str
    description: str
    rules: Optional[str]
    players: Optional[str]
    duration: Optional[str]
    age_limit: Optional[int]
    release: Optional[str]
    author: Optional[str]

    fake = Faker()

    def __init__(self):
        self.__name_gen()
        self.__description_gen()
        self.__rules_gen()
        self.__players_gen()
        self.__duration_gen()
        self.__age_limit_gen()
        self.__release_gen()
        self.__author_gen()

    def __name_gen(self):
        self.name = f"{self.fake.word()}{uuid4()}"

    def __description_gen(self):
        self.description = self.fake.text()

    def __rules_gen(self):
        gen = self.fake.boolean()
        if gen:
            self.rules = self.fake.text()
        else:
            self.rules = None

    def __players_gen(self):
        max_players = random.randint(1, 20)
        min_players = random.randint(1, 20)
        if max_players >= min_players:
            if max_players == min_players:
                self.players = str(max_players)
            else:
                self.players = f'{min_players} - {max_players}'
        else:
            self.players = None

    def __duration_gen(self):
        dur = random.randint(0, 90)
        if dur != 0:
            self.duration = f'{dur}+ minutes'
        else:
            self.duration = None

    def __age_limit_gen(self):
        self.age_limit = random.randint(1, 25)

    def __release_gen(self):
        gen = self.fake.boolean()
        if gen:
            self.release = str(self.fake.date_between_dates(date_start=datetime.date(2005, 1, 1),
                                                            date_end=datetime.date.today()))
        else:
            self.release = None

    def __author_gen(self):
        gen = self.fake.boolean()
        if gen:
            self.author = self.fake.name()
        else:
            self.author = None

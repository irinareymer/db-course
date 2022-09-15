from faker import Faker


class Collection:
    name: str

    fake = Faker()

    def __init__(self):
        self.__name_gen()

    def __name_gen(self):
        self.name = self.fake.word()

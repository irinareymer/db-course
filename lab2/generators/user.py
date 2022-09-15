import datetime
from faker import Faker
from uuid import uuid4


class User:

    email: str
    password: str
    username: str
    date_of_birth: datetime.date

    fake = Faker()

    def __init__(self):
        self.__email_gen()
        self.__pass_gen()
        self.__username_gen()
        self.__date_of_birth_gen()

    def __email_gen(self):
        self.email = f"{uuid4()}{self.fake.profile()['mail']}"

    def __pass_gen(self):
        self.password = self.fake.sha256()

    def __username_gen(self):
        self.username = f"{self.fake.profile()['username']}{uuid4()}"

    def __date_of_birth_gen(self):
        self.date_of_birth = self.fake.profile()['birthdate']

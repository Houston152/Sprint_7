import random
from faker import Faker


class GenerationData:
    def generation_email(self):
        faker = Faker()
        email = faker.email()
        return email

    def generation_password(self):
        password = random.randint(100000, 999999)
        return password

    def generation_name(self):
        faker = Faker()
        name = faker.name()
        return name


class StorageData:
    order_data = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "address": "Moscow, Lenina, 15",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 1,
        "deliveryDate": "2020-06-06",
        "comment": "Привезите быстрее самокат!",
    }

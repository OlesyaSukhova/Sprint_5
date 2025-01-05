from faker import Faker
import random
faker = Faker()

def generate_random_email():
    name = faker.first_name()
    surname = faker.last_name()
    group_number = faker.random.randint(1, 20)
    number = faker.random.randint(100, 999)
    return name + surname + str(group_number) + str(number) + '@mail.ru'

def generate_random_password():
    password = faker.password(length=6)
    return password

def generate_random_invalid_password():
    password = faker.password(length=5)
    return password
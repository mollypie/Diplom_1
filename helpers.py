import random
import string


class Helpers:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def create_name():
        return Helpers.generate_random_string(8)

    @staticmethod
    def create_price():
        return random.randint(0, 500)

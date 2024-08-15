import random


def generate_random_digit(length=6):
    digits = "0123456789"
    return "".join(random.choice(digits) for _ in range(length))

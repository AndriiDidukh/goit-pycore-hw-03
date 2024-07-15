import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or min > max or quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers


print(get_numbers_ticket(1, 1000, 10))
print(get_numbers_ticket(1, 10, 9))
print(get_numbers_ticket(-5, 55, 10))
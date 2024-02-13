from utils import is_prime

number = 17
if is_prime(number):
    print(f"{number} є простим числом.")
else:
    print(f"{number} не є простим числом.")
from utils import is_prime, is_power_of_five

number = 125
if is_power_of_five(number):
    print(f"{number} є степенем п'ятірки.")
else:
    print(f"{number} не є степенем п'ятірки.")
from utils import is_prime, is_power_of_five, is_power_of_two

number = 64
if is_power_of_two(number):
    print(f"{number} є степенем двійки.")
else:
    print(f"{number} не є степенем двійки.")
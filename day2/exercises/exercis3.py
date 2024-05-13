import string
import random

STRING_LENGTH = 5

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

random_string = generate_random_string(STRING_LENGTH)
print(random_string)

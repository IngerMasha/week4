import re


def return_numbers(string):
    numbers = re.findall(r'\d', string)
    numbers_string = ''.join(numbers)
    return int(numbers_string)
def validate_name(full_name):
    pattern = r'^[A-Z][a-z]+\s[A-Z][a-z]+$'

    if re.match(pattern, full_name):
        return True
    else:
        return False

result = return_numbers('k5k3q2g5z6x9bn')
print("Expected output:", result)
full_name = input("Enter your full name:  ")

if validate_name(full_name):
    print("Your name is valid.")
else:
    print("Invalid name format. Please enter your full name with the first letter of each name capitalized.")

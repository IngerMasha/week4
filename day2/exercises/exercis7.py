from faker import Faker
import random
fake = Faker()
users = []
def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': random.choice(['en', 'fr', 'es', 'de', 'it'])
    }
    users.append(user)

for _ in range(5):
    add_user()
print(users)

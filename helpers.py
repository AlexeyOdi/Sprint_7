import random
import string

def generate_courier():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    courier_data = {}

    courier_data['login'] = generate_random_string(10)
    courier_data['password'] = generate_random_string(10)
    courier_data['first_name'] = generate_random_string(10)

    return courier_data
import re
import string
import random
import rstr


def random_generator(size, chars = string.ascii_lowercase + string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))


def get_test_email():
    return random_generator(12) + '@testmail.com'


def get_test_password(chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation):
    return ''.join(random.choice(chars) for x in range(10))


def generate_pattern_string(pattern):
    return rstr.xeger(pattern)

def get_test_username():
    return random_generator(7) + ' ' + random_generator(8)


def get_test_mobile_number(chars = string.digits):
    return ''.join(random.choice(chars) for x in range(10))


def get_random_gender():
    return ['M', 'F', 'O'][random.randrange(0, 3)]


def get_random_status():
    return ["active", "inactive", "suspended", "golden", "silver", "diamond", "prime"][random.randrange(0, 7)]



def getRandomDates():
    return str(str(random.randrange(2006, 2023))+ '-'+ str(formatter(random.randrange(1, 12))) + '-' + str(formatter(random.randrange(1, 30))) + ' ' +
               str(formatter(random.randrange(1,24))) + ':' + str(formatter(random.randrange(0, 60))) + ':' + str(formatter(random.randrange(0, 60))))


def formatter(value):
    if value < 10:
        return '0'+str(value)
    else:
        return value

if __name__ == '__main__':
    print(generate_pattern_string(r'^[A-Z]{3}-\d{3}$'))
    print(generate_pattern_string(r'^[A-Z]{3}-\d{3}$'))
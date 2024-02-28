# find characters, integers, special character and space in a string

import re
import string

temp_str = "today is 1st feb 2024."

def find_char_count(temp_str):
    char_count = len(re.findall('[a-z]', temp_str))
    digit_count = len(re.findall('\d', temp_str))
    space_count = len(re.findall('\s', temp_str))
    special_count = len(re.findall('', temp_str))

    return char_count, digit_count, space_count, special_count


print(find_char_count(temp_str))
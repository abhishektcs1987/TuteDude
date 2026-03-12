import math_utils
from math_utils import square

print(math_utils.add(1, 2))       
print(math_utils.subtract(1, 2))
print(math_utils.square(2))

import string_utils
print(string_utils.capitalize_words("hello world"))
print(string_utils.reverse_string("hello world"))
print(string_utils.word_count("hello world"))

import shop_package.discount as disc
from shop_package.billing import calculate_total

print(disc.apply_discount(1000, 10))
print(calculate_total([100, 200, 300]))
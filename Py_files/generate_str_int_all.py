import random
import string


def gen_rand_str(length):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for _ in range(length))
    print(length, "Random leTteRs: >>>", rand_str)


def gen_rand_low_str(length):
    letters = string.ascii_lowercase
    rand_str = ''.join(random.choice(letters) for _ in range(length))
    print(length, "Random letters: >>>", rand_str)


def gen_rand_upp_str(length):
    letters = string.ascii_uppercase
    rand_str = ''.join(random.choice(letters) for _ in range(length))
    print(length, "Random LETTERS: >>>", rand_str)


def gen_rand_num(r):
    numbers = string.digits
    rand_num = ''.join(random.choice(numbers)for _ in range(r))
    print(r, "Random digits : >>>", rand_num)


def get_rand_all(r):
    characters = string.ascii_letters + string.digits + string.punctuation
    rand_all = ''.join(random.choice(characters) for _ in range(r))
    print(r, "Random all    : >>>", rand_all)


gen_rand_str(31)

gen_rand_num(31)
get_rand_all(31)


## Response e.g.:
#> 31 R Letters: >>> FffDnoAhkSTmbduiOtnFdiRNxUwFZTL
#> 18 R Digits : >>> 447324461738687389
#> 20 R All    : >>> ZG?R"WmRxf_aQMz]8e\g

import random
import string


def gen_rand_str(length):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for _ in range(length))
    print(length, "R Letters: >>>", rand_str)


def gen_rand_num(r):
    numbers = string.digits
    rand_num = ''.join(random.choice(numbers)for _ in range(r))
    print(r, "R Digits : >>>", rand_num)


def get_rand_all(r):
    characters = string.ascii_letters + string.digits + string.punctuation
    rand_all = ''.join(random.choice(characters) for _ in range(r))
    print(r, "R All    : >>>", rand_all)


gen_rand_str(31)
gen_rand_num(18)
get_rand_all(20)

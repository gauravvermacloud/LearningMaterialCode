################# List Comprehenion ################

import math
words = "This is a sentence with words"

list_of_words = words.split()


def first_chat(x: str) -> str:
    return x[0]


lst_len = [len(x) for x in list_of_words]

print(lst_len)

lst_first_char = [first_chat(x) for x in list_of_words]

print(lst_first_char)

lst_fact = [math.factorial(x) for x in range(5)]
print(lst_fact)

############### Set Comprehension ################

set_len = {len(x) for x in list_of_words}

print(set_len)

set_first_char = {first_chat(x) for x in list_of_words}

print(set_first_char)

set_fact = {math.factorial(x) for x in range(5)}
print(set_fact)


########### Dictionary Comprehension ###############

dict = {x: math.factorial(x) for x in range(5)}
print(dict)


############### filters ########################

def is_prime(x):
    prime = True
    for n in range(2, x):
        if (x % n == 0):
            return False

    return prime


lst_prime = [x for x in range(101) if is_prime(x)]
print(lst_prime)


dict_prime_factorial = {x: math.factorial(
    x) for x in range(101) if is_prime(x)}

print(dict_prime_factorial)

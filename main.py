import random
import string

def rand_letters(c):
    i = 0
    abc = string.ascii_lowercase
    while i < c:
        print(random.choice(abc))      #Випадково вибирамо одну літеру з abc.
        i = i + 1


rand_letters(10)

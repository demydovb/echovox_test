""" A new object

1. Write a function that given an object returns a tuple of the same object and a new one with
the added property : type: test
2. If you used the spread/unpack operator, do it without.
"""

from copy import deepcopy

def add_property_to_obj(obj):
    new_obj = deepcopy(obj)
    setattr(new_obj, 'type', 'test')
    return obj, new_obj


""" Data analytics
1. Write a function that given a csv file output a list containing each row. What if the file is
huge.
2. You have a long series of elements coming from an unknown source.
Write a function that applies another function on each element of the list. (You can do this
exercise using the function from the previous exercise)
"""

#1
import csv

def csv_parser(csv_file):
    with open(csv_file, "rU") as data:
        reader = csv.reader(data)
        for line in reader:
            print(line)

# Approach for huge files
import pandas as pd
def pandas_csv_parser(csv_file):
    row_count = 100
    for chunk in pd.read_csv(csv_file, chunksize=row_count, iterator=True):
        for i, row in chunk.iterrows():
            print(row)
            print(" ")

#2

def map_csv_parser(sources):
    map(pandas_csv_parser, sources)

""" Primes

1. Write a function returning all factors of numbers from 2 to 100
2. Print the prime numbers with as little change as possible of the function you wrote for part 1.
"""

#1
def find_factors():
    factors = {}
    for number in range(2, 101):
        factors[number] = []
        for i in range(1, number+1):
            if number % i == 0:
                factors[number].append(i)
    return factors


#2
def find_factors_and_prime():
    factors = {}
    prime_numbers = []
    for number in range(2, 101):
        factors[number] = []
        is_prime = True
        for i in range(1, number+1):
            if number % i == 0:
                factors[number].append(i)
                if i != 1 and i != number:
                    is_prime = False
        if is_prime:
            prime_numbers.append(number)
    print("Prime numbers: {}".format(prime_numbers))
    return factors

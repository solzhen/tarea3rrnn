import numpy as np


def binary_gen():
    return np.random.randint(0, 2)

def ordinal_alphabet_gen():
    return np.random.randint(32, 123)

def integer_ten_gen():
    return np.random.randint(10)

def integer_four_gen():
    return np.random.randint(4)
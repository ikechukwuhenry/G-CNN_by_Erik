import numpy as np
import torch


class C4:

    @staticmethod
    def product(r: int, s: int) -> int:
        try:
            valid_r = int(r)
            valid_s = int(s)
            print("code")
            return (valid_r + valid_s) % 4
        except ValueError:
            print("Invalid Input")
            
    @staticmethod
    def inverse(r: int) -> int:
        try:
            valid_r = int(r)
            for n in range(4):
                if (valid_r + n)  % 4 == 0:
                    return n
        except ValueError:
            print("Invalid Input")


# Testing with invalid input
print(C4.product(1, 'a'))
print(C4.product(0, 0))
print(C4.product(2, 3))

# Testing with valid Inputs
# assert C4.product(1, 3) == 0
# assert C4.product(0, 0) == 0
# assert C4.product(2, 3) == 1
print("group inverse element")
print(C4.inverse(2))
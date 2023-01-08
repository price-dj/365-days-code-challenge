# define a function that takes an integer, if even
# divides by 2, if odd *3 + 1
import sys
import numpy as np


def collatz1(num: int):
    if num % 2 == 0:
        return num / 2
    elif num % 2 == 1:
        return num * 3 + 1


def collatz2(num: int):
    res = [num]
    while num != 1:
        num = int(collatz1(num))
        res.append(num)
    return res


def main():
    try:
        num = int(input("Input: "))
        res = collatz2(num)
        print("Output: ", res)
    except ValueError:
        print("Wrong input, exiting")
        sys.exit(-1)


if __name__ == '__main__':
    main()
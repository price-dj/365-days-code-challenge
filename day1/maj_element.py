# package which sole purpose
# it is to calc mode, most common, majority element
# a np array, or list
import numpy as np
import sys


def majority_element(arr):
    """
    returns majority element/most common/mode
    assumed to exist ie assuming there are no ties
    :param arr: np array or list
    :return: int (the element that is the mode)
    """

    nums = list(map(int, arr))
    #print(nums)
    return max(nums, key=nums.count)


def main():
    try:
        arr = str((input("Input: "))).strip('[').strip(']').split(sep=',')
        #print("you entered ", arr)
        res = majority_element(arr)
        print("Output: ", res)
    except ValueError:
        print("Wrong input, exiting")
        sys.exit(-1)


if __name__ == '__main__':
    main()
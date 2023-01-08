# package which sole purpose
# it is to calc mode, most common, majority element
# a np array, or list


def majority_element(arr):
    """
    returns majority element/most common/mode
    assumed to exist ie assuming there are no ties
    :param arr: np array or list
    :return: int (the element that is the mode)
    """
    nums = list(arr)
    return max(nums, key=nums.count)
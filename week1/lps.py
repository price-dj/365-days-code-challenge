import numpy as np

def longest_palindrome_substring_slow(s: str):
    """
    Essentially python implementation of slow algo pseudocode from wikipedia
    :param s:
    :return:
    """

    # need to insert bogus '|' chars in between each char and at boundaries
    s_prime = '|' + '|'.join(list(s)) + '|'
    palindrome_radii = np.zeros(len(s_prime))
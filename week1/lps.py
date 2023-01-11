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

    centre = 0

    while centre < len(s_prime):
        # Determine the longest palindrome starting at Center - Radius and going to Center + Radius
        radius = 0
        while centre - radius + 1 >= 0 \
            and centre + radius + 1 < len(s_prime) \
            and s_prime[centre + radius + 1] == s_prime[centre - radius + 1]:

            radius += 1
            #print(radius)

        # Save the radius of the longest palindrome in the array
        palindrome_radii[centre] = 2 * radius

        centre += 1

    print(palindrome_radii)
    longest_palindrome_in_s_prime = max(palindrome_radii)
    longest_palindrome_in_s = int((longest_palindrome_in_s_prime-1) / 2)

    return longest_palindrome_in_s


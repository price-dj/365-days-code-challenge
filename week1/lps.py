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

        # Save the radius of the longest palindrome in the array
        palindrome_radii[centre] = 2 * radius

        centre += 1

    palindrome_radii = (palindrome_radii - 1) // 2
    # for s_prime get all max radii and indexes
    centres = [centre for centre, item in enumerate(palindrome_radii) if item == max(palindrome_radii)]

    lps_results = []

    for centre in centres:
        radius = int(palindrome_radii[centre])
        lps_prime = s_prime[centre - radius + 1: centre + radius + 1]
        lps = lps_prime.strip('|').split('|')
        lps = ''.join(lps)
        lps_results.append(lps)

    return lps_results


# def longest_palindrome_substring_manacher(s: str):
#     """
#
#     :param s:
#     :return:
#     """
#
#     s_prime = '|' + '|'.join(list(s)) + '|'
#     palindrome_radii = np.zeros(len(s_prime))
#
#     centre = 0
#     radius = 0
#
#     while centre < len(s_prime):
#         # At the start of the loop, Radius is already set to a lower-bound for the longest radius.
#         # In the first iteration, Radius is 0, but it can be higher on later iterations.
#
#         # Determine the longest palindrome starting at Center-Radius and going to Center+Radius
#
#         while centre - radius + 1 >= 0 \
#                 and centre + radius + 1 < len(s_prime) \
#                 and s_prime[centre + radius + 1] == s_prime[centre - radius + 1]:
#             radius += 1
#
#         # Save the radius of the longest palindrome in the array
#         palindrome_radii[centre] = radius
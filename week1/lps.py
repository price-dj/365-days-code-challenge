import math

import numpy as np


def longest_palindrome_substring_slow(s: str):
    """
    Essentially python implementation of slow algo pseudocode from wikipedia
    :param s: string to be searched for longest palindromic strings
    :return: list of all longest palindromic strings
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

    print(palindrome_radii)
    palindrome_radii = (palindrome_radii - 1) // 2
    # for s_prime get all max radii and indexes
    centres = [centre for centre, item in enumerate(palindrome_radii) if item == max(palindrome_radii)]

    lps_results = []

    for centre in centres:
        radius = int(palindrome_radii[centre])
        print(centre, radius)
        lps_prime = s_prime[centre - radius + 1: centre + radius + 1]
        lps = lps_prime.strip('|').split('|')
        lps = ''.join(lps)
        lps_results.append(lps)

    return lps_results



def longest_palindrome_substring_manacher(s: str):
    """

    :param s:
    :return:
    """
    #print(s)
    s_prime = list('@#' + '#'.join(list(s)) + '#$')
    pal_radii = list(np.zeros(len(s_prime), dtype=np.int))
    #print(s_prime)

    max_pal_len = 0
    start = 0
    max_right = 0
    centre = 0

    for pos in range(1, len(s_prime) - 1):
        if pos < max_right:
            pal_radii[pos] = min(max_right - pos, pal_radii[2 * centre - pos])

        # expanding along the centre
        while s_prime[pos + pal_radii[pos] + 1] == s_prime[pos - pal_radii[pos] - 1]:
            pal_radii[pos] += 1

        # updating centre and its bound
        if pos + pal_radii[pos] > max_right:
            centre = pos
            max_right = pos + pal_radii[pos]

        # updating ans
        if pal_radii[pos] > max_pal_len:
            start = int((pos - pal_radii[pos] - 1) / 2)
            max_pal_len = pal_radii[pos]


    # print the longest palindromic substring
    print("The longest palindromic substring is: ", end="")
    printSubstring(s, start, start + max_pal_len - 1)
    return

#
# A function to print a substring.
def printSubstring(str, left, right):
    for i in range(left, right + 1):
        print(str[i], end="")
    print("")

def all_longest_palindromic_substrings_manacher(s: str):
    """

    :param s:
    :return:
    """
    # need to insert bogus '|' chars in between each char and at boundaries
    s_prime = '|' + '|'.join(list(s)) + '|'
    pal_radii = [0] * len(s_prime)

    centre = 0
    radius = 0

    while centre < len(s_prime):
        # // At the start of the loop, Radius is already set to a lower-bound for the longest radius.
        # // In the first iteration, Radius is 0, but it can be higher on later iterations.
        # // Determine the longest palindrome starting at Center-Radius and going to Center+Radius
        while centre - (radius + 1) >= 0 \
                    and centre + (radius + 1) < len(s_prime) \
                    and s_prime[centre - (radius + 1)] == s_prime[centre + (radius + 1)]:
            radius += 1

        # // Save the radius of the longest palindrome in the array
        pal_radii[centre] = radius

        # // Below, Center is incremented.
        # // If any precomputed values can be reused, they are.
        # // Also, Radius may be set to a value greater than 0

        old_centre = centre
        old_radius = radius
        centre += 1
        # // Radius' default value will be 0, if we reach the end of the following loop.
        radius = 0
        while centre <= old_centre + old_radius:
            # // Because Center lies inside the old palindrome and every character inside
            # // a palindrome has a "mirrored" character reflected across its center, we
            # // can use the data that was precomputed for the Center's mirrored point.
            mirrored_centre = old_centre - (centre - old_centre)
            max_mirrored_radius = old_centre + old_radius - centre

            if pal_radii[mirrored_centre] < max_mirrored_radius:
                # // the palindrome centered at MirroredCenter is entirely contained in the palindrome centered at OldCenter
                # // So, MirroredCenter and Center have the same sized palindrome
                pal_radii[centre] = pal_radii[mirrored_centre]
                centre += 1

            elif pal_radii[mirrored_centre] > max_mirrored_radius:
                # // The palindrome at MirroredCenter is extends beyond the palindrome at OldCenter
                # // The palindrome at Center must end at the edge of the OldCenter palindrome
                # // Otherwise, the palindrome at OldCenter would be bigger
                pal_radii[centre] = max_mirrored_radius
                centre += 1

            else:
                # // Since the palindrome at MirroredCenter ends exactly at the edge of the palindrome centered at OldCenter,
                #   // the palindrome at Center might be bigger
                #  // Set Radius to the minimum size of the palindrome at Center so it doesn't recheck unnecessarily
                radius = max_mirrored_radius
                break
            #print("here")

    # get the palindroms
    if len(s) % 2 == 0:
        pal_radii = pal_radii[0::2]
    else:
        pal_radii = pal_radii[1::2]

    centres = [centre for centre, item in enumerate(pal_radii) if item == max(pal_radii)]

    lps_res = []
    for centre in centres:
        pal_length = pal_radii[centre]
        start = centre - int(pal_length / 2)
        end = start + pal_length
        lps = s[start:end]
        lps_res.append(lps)

    return lps_res





if __name__ == '__main__':
    #s = "abracadabra"
    #s = 'book'
    s = 'r111a'
    #longest_palindrome_substring_manacher(s)
    print(all_longest_palindromic_substrings_manacher(s))

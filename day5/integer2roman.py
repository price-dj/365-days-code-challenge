
# use a dict of known values to reference

# do loop of division and remainder

def integer2roman(number: int):
    """

    :param number: int (decimal) 1<= number <= 3999
    :return: roman numeral
    """
    decimals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman_numerals = {1 : "I" , 4 : "IV", 5: "V", 9 : "IX", 10 : "X",40 : "XL", 50 : "L",
                     90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M"}

    roman_numeral_result = []


    # initialise remainder
    remainder = number
    while remainder != 0:
        # which member of decimals list is either == or < to remainder
        for i in range(len(decimals)):
            if remainder == decimals[i]:
                roman_num = roman_numerals[decimals[i]]
                roman_numeral_result.append(roman_num)
                remainder = 0
                break
            elif decimals[i] < remainder:
                quotient = int(remainder // decimals[i])
                remainder = remainder % decimals[i]
                roman_num = roman_numerals[decimals[i]] * quotient
                roman_numeral_result.append(roman_num)

    return "".join(roman_numeral_result)


if __name__ == "__main__":
    print(integer2roman(1976))
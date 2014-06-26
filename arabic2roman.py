#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Programm to convert a number to roman numeral system

'''

__author__ = 'Saverio Scavelli'
__copyright__ = "Copyright 2014, Saverio Scavelli"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Saverio Scavelli"
__email__ = "saverio.scavelli@googlemail.com"
__status__ = "Development"


'''
A list of tuples containing an integer and the corresponding roman-numeral symbol.
'''
roman_list = [
    (1000, "M"), (900, "CM"),
    (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"),
    (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"),
    (5, "V"), (4, "IV"),
    (1, "I")
]


def int_to_roman(integer):
    '''
        Core function of the program.
        the 'integer' parameter is the number to be converted.
        the 'result' list will be need to contains the results of each for loop.
        the 'cnt_parens' field will be increased every time the built-in function divmod() return a remainder == 0.
        This is necessary because in the roman-numeral system every number over 3999 must be enclosed in two
        extra signs e.g. 50.000 will be (XII) MM, or 12*4000+1000+1000.
        The built-in divmod() function does the actual work, it take two (non complex) numbers as arguments and return
        a pair of numbers consisting of their quotient and remainder. Iterating over 'roman_list', every time the
        quotient > 0 the corresponding roman-numeral symbol will be added to 'roman_result' so many times as the quotient value.
        e.g.
        >>>divmod(2000,1000)
        >>>(2,0)
        That will be MM
    '''
    result = []
    cnt_parens = 0
    while integer:
        integer, num = divmod(integer, 4000)
        roman_result = ""
        for value, rchar in roman_list:
            count, num = divmod(num, value)
            roman_result += count * rchar
        if roman_result:
            result.append('{}{}{}'.format(
                '(' * cnt_parens, roman_result, ')' * cnt_parens))
        cnt_parens += 1
    return ' '.join(result[::-1])


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Convert an arabic number (decimal system) "
                                                 "to a roman numeral-system number. ")
    parser.add_argument("number", help="Give a integer as argument.", type=int)
    args = parser.parse_args()
    print int_to_roman(args.number)

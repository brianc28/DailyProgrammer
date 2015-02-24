# [2015-02-18] Challenge #202 [Intermediate] Easter Challenge
# http://redd.it/2wbvuu

# Description:

# Given the year - Write a program to figure out the exact date of Easter for that year.

# Input:
#   A year.

# Output:
#   The date of easter for that year.

# Challenge:
#   Figure out easter for 2015 to 2025.


# Solution:
# using the "Anonymous Gregorian algorithm" from https://en.wikipedia.org/wiki/Computus

import math
import datetime


def easter_day(y):
    a = y % 19
    b = math.floor(y / 100)
    c = y % 100
    d = math.floor(b / 4)
    e = b % 4
    f = math.floor( (b + 8) / 25 )
    g = math.floor( (b - f + 1 ) / 3 )
    h = ( (19 * a) + b - d - g + 15) % 30
    i = math.floor( c / 4)
    k = c % 4
    l = (32 + (2 * e) + (2 * i) - h - k) % 7
    m = math.floor((a + (11 * h) + (22 * l)) / 451)
    month = math.floor((h + l - (7 * m) + 114) / 31)
    day = ((h + l - (7 * m) + 114) % 31) + 1

    edate = datetime.date(y, month, day)

    print("Easter(In Gregorian dates) of", y, "is on", edate.strftime("%B"), edate.strftime("%d"))


    # print(y, a, b, c, d, e, f, g, h, i, k, l, m, month, day)


for year in range(2015, 2026):
    easter_day(year)


#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
Kartik. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Kartik
Semester: Fall 2024
Description: Implements functionality to calculate next and previous days, as well as leap year checks and month limits.
'''

import sys

def leap_year(year: int) -> bool:
    """
    Check whether the following year is a leap year or not
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """
    The following will return the maximum number of days in a given month.
    """
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    return month_days[month]

def after(date: str) -> str:
    """
    this function will return the date for the next day in DD/MM/YYYY format.
    """
    day, month, year = (int(x) for x in date.split('/'))
    day += 1

    if day > mon_max(month, year):
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1

    return f"{day:02}/{month:02}/{year}"

def before(date: str) -> str:
    """
    In DD/MM/YYYY format return the date for the previous day
    """
    day, month, year = map(int, date.split('/'))
    day -= 1

    if day == 0:
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        day = mon_max(month, year)

    return f"{day:02}/{month:02}/{year}"

if __name__ == "__main__":
    # Tests for Milestone 1 functions
    print(after("28/02/2020"))  # Expect "29/02/2020" (Leap Year)
    print(before("01/03/2020")) # Expect "29/02/2020" (Leap Year)
    print(mon_max(2, 2020))     # Expect 29 (Leap Year)
    print(mon_max(2, 2021))     # Expect 28 (Non-Leap Year)

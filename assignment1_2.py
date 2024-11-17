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
Description: Implements functionality to calculate next and previous days, validate dates, and iterate days.
'''

import sys

def leap_year(year: int) -> bool:
    """
    If it is a leap year it will return True, else false.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """
    It will return the maximum number of days in the mentioned month, also including the check for leap year.
    """
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    return month_days[month]

def after(date: str) -> str:
    """
    The following is going to return the date for the upcoming day in DD/MM/YYYY string format.
    Refactored to use leap_year() and mon_max().
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
    Next returns the date for the previous day in DD/MM/YYYY string format.
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

def valid_date(date: str) -> bool:
    """
       Foloowing will check whether the given date is valid in DD/MM/YYYY format, or not.
    """
    # Ensuring the format is correct, also containing exactly two slashes
    if len(date) != 10 or date.count('/') != 2:
        return False

    try:

        day, month, year = (int(x) for x in date.split('/'))

        # Verify if the year is within the given range
        if not (1539 <= year <= 2999):
            return False

        # Validating month and day
        if not (1 <= month <= 12 and 1 <= day <= mon_max(month, year)):
            return False

        return True
    except ValueError:
        return False  #Return False if any part of the date is invalid

def day_iter(start_date: str, num: int) -> str:
    """
    Perform forward or backward by 'num' days starting from 'start_date'.
    """
    current_date = start_date
    step = after if num > 0 else before
    for _ in range(abs(num)):
        current_date = step(current_date)
    return current_date

if __name__ == "__main__":
    # Check script compatibility
    pass

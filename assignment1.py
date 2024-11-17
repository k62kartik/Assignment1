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
    Verify if a year is a leap year or not.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """
    Return the maximum number of days in a specified month.
    """
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    return month_days[month]

def after(date: str) -> str:
    """
    In DD/MM/YYYY format return the daye for the next date.
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
    For the previous day return the date in DD/MM/YYYY format.
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
    Ensuring if the date is in correct formate that is DD/MM/YYYY
    """
    # Ensure format is correct
    if len(date) != 10 or date.count('/') != 2:
        return False

    try:
        # Split the date and convert parts to integers
        day, month, year = (int(x) for x in date.split('/'))

        #Checking if the year is within the allowed range or not
        if not (1539 <= year <= 2999):
            return False

        # Check if the month and day are valid
        if not (1 <= month <= 12 and 1 <= day <= mon_max(month, year)):
            return False

        return True  # If all checks pass then the date is correct
    except ValueError:
        return False  # If any part of the date is wrong or incorrect then return False 

def day_iter(start_date: str, num: int) -> str:
    """
    Iterate forward or backward by 'num' days starting from 'start_date'.
    """
    current_date = start_date
    step = after if num > 0 else before  # Choose after() for the positive and before() for negative
    for _ in range(abs(num)):
        current_date = step(current_date)
    return current_date  # Return the final date

if __name__ == "__main__":
    # Minimal main block for check script compatibility
    pass

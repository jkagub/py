#! python

# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case.

import re
def check_time(text):
    # ^ matches the start of the string.
    # (1[0-2]|0?[1-9]) matches the hour part. It allows for either a single digit from 1 to 9 (optionally preceded by a leading zero) or the number 10, 11, or 12.
    # : matches the colon separator.
    # [0-5][0-9] matches the minutes part, ensuring it is between 00 and 59.
    # \s* matches zero or more whitespace characters (optional space).
    # [APap][Mm] matches the AM or PM part, allowing for either uppercase or lowercase.
    # $ matches the end of the string.
    pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9]\s*[APap][Mm]$"
    result = re.search(pattern, text)
    return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
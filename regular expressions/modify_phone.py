#! python
import re

#We're working with a CSV file, which contains employee information.
#  Each record has a name field, followed by a phone number field, and a role field.
#  The phone number field contains U.S. phone numbers,
#  and needs to be modified to the international format, with "+1-" in front of the phone number.

import re
def transform_record(record):
    # \d matches any digit.
    # {3} specifies that the preceding element (in this case, \d) should occur exactly 3 times.
    # - matches the hyphen character literally.
    # \d{3,} specifies that the preceding pattern (again, \d) should occur at least 3 times, but it can occur more times.
    # -? matches the hyphen character optionally, meaning it may or may not be present in the string.
    # {4} specifies that the preceding element (\d) should occur exactly 4 times.
    new_record = re.sub(r"(\d{3}-\d{3,}-?\d{4})", r"+1-\1", record)
    return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
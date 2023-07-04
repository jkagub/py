#! python
import re

#Here, we wanted to match on strings that had.com in them, but we match a string with something else in it. That's not what we wanted.
print(re.search(r".com", "welcome"))
#By escaping the dot, it no longer matched the word Welcome
print(re.search(r"\.com", "welcome"))
# try something that should actually match.
print(re.search(r"\.com", "mydomain.com"))
#\w matches any alphanumeric character including letters, numbers, and underscores.
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))
# \d for matching digits
print(re.search(r"\d*", "3 is a digit"))
# \s for matching whitespace characters like space, tab or new line, \b for word boundaries and a few others.
print(re.search(r"\d*", "3 is a digit"))

#code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.
def check_character_groups(text):
#The regular expression pattern r"\b\w+\s+\w+\b" matches groups of one or more word characters (alphanumeric or underscore) separated by one or more whitespace characters.
#The \b at the beginning and end of the pattern matches word boundaries to ensure that the pattern matches whole words.
#\w+ matches one or more word characters.
#\s+ matches one or more whitespace characters.
    result = re.search(r"\b\w+\s+\w+\b", text)
    return result is not None

print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

#! python
import re

# The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc.

def check_web_address(text):
    # ^ matches the start of the string.
    # (www\.)? matches an optional "www." at the beginning.
    # [A-Za-z0-9_-]+ matches one or more alphanumeric characters, underscores, or hyphens.
    # \. matches a period.
    # [A-Za-z]{2,3} matches two or three letters.
    # $ matches the end of the string.
    pattern = r"^(www\.)?[A-Za-z0-9_-]+\.[A-Za-z]{2,3}$"
    result = re.search(pattern, text)
    return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

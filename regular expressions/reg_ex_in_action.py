#! python
import re

#you had a list of all the countries in the world and you want to check which of those names start and end in a
print(re.search(r"A.*a", "Argetina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))
# validate if the string is a valid variable name in Python
# It can contain any number of letters numbers or underscores, but it can't start with a number.

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
# Once we use a space, it stops being a valid variable name
print(re.search(pattern, "this isn't a valid variable name"))

print(re.search(pattern, "my_variable1"))

print(re.search(pattern, "2my_variable1"))

# code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 

def check_sentence(text):
    result = re.search(r"^[A-Z][a-z ]*[.?!]$", text)
    return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
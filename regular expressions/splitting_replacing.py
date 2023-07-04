#! python
import re

print(re.split(r"[.?!]", "One sentece. Another one? And the last one!"))

#  If we want our split list to include the elements that we're using to split the values we can use capturing parentheses like this.
print(re.split(r"([.?!])", "One sentece. Another one? And the last one!"))

#  RE module is called "sub" is used for creating new strings by substituting all or part of them for a different string, similar to the replace string method but using regular expressions for both the matching and the replacing.
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))

# example using sub where we use regular expressions for the replacing.
#  For that, we'll go back to our code that switched the order of names of people and use sub to create the new string.
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))

# We want to split a piece of text by either the word "a" or "the", as implemented in the following code.
print(re.split(r"the|a", "One sentence. Another one? And the last one!"))
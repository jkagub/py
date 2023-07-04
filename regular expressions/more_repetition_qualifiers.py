#! python

import re

# In this case, we're looking for letters that are repeated five times, and ghost has five letters, so it matched our pattern.
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# use the findall function to find more matches
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# using \b, which matches word limits at the beginning and end of the pattern, to indicate that we want full words
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
# if we wanted to match a range of five to ten letters or numbers, we could use an expression like this one.
print(re.findall(r"\w{5,10}", "I really like strawberries"))
# These ranges can also be open ended.
# A number followed by a comma means at least that many repetitions with no upper boundary limited only by the maximum repetitions in the source text.
print(re.findall(r"\w{5,}", "I really like strawberries"))
#  a comma followed by a number means from zero up to that amount of repetitions.
print(re.findall(r"s\w{,20}", "I really like strawberries"))

# The long_words function returns all words that are at least 7 characters. 
def long_words(text):
    pattern = r"\w{7,}"
    result = re.findall(pattern, text)
    return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []



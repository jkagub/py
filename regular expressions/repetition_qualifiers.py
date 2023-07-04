#! python

import re

#a dot followed by a star. This means that it matches any character repeated as many times as possible including zero.
print(re.search(r"Py.*n", "Pygmalion"))
#Remember, the Star takes as many characters as possible. In programming terms, we say that this behavior is greedy.
print(re.search(r"Py.*n", "Python Programming"))
#If we only wanted our patterns match letters, we should have used the character class instead like this.
print(re.search(r"Py[a-z]*n", "Python Programming"))
#Remember how we said that zero times is also a possibility? That will let the string pin also match our pattern. Let's try that out.
print(re.search(r"Py[a-z]*n", "Pyn"))
#The plus character matches one or more occurrences of the character that comes before it. So we had the pattern O plus L plus. Let's check it against a few words.
#In this case, there was one occurrence of each. In the match pattern shows us the shortest possible matching string.
print(re.search(r"o+l+", "goldfish"))
#Here, there were two of each
print(re.search(r"o+l+", "woolly"))
#while our string here had an O and an L, it had another character in between them. Because of this, it doesn't match the search pattern.
print(re.search(r"o+l+", "boil"))

#The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False.
def repeating_letter_a(text):
    #result = re.search(r"a.*a", text, re.IGNORECASE)
    #return result is not None
    result = re.search(r"[Aa].*a+", text)
    return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

#The question mark symbol is yet another multiplier. It means either zero or one occurrence of the character before it. Let's see how this works.
#The P wasn't present but with the question mark we marked it as optional. So we still got a match.
print(re.search(r"p?each", "To each their own"))
#the P was present and so match included it.
print(re.search(r"p?each", "I like peaches"))
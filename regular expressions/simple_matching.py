#! python
import re

#result = re.search(r"aza", "plaza")
#print(result)

#print(re.search(r"^x", "xenon"))
#print(re.search(r"p.ng", "penguin"))
#print(re.search(r"p.ng", "clapping"))
#print(re.search(r"p.ng", "sponge"))

#code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
def check_aei (text):
    result = re.search(r"a.e.i", text, re.IGNORECASE)
    return result != None

print(check_aei("Academia")) # True
print(check_aei("Aerial")) # False
print(check_aei("Paramedic")) # True
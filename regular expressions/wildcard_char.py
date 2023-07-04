#! python
import re

#match the word Python but allow for both lowercase or uppercase p.
#print(re.search(r"[Pp]ython", "Python"))
#use lowercase a to lowercase z to state any lowercase letter. So if we wanted to look for the string way preceded by any letter.
#print(re.search(r"[a-z]way", "The end of the highway"))
#print(re.search(r"[a-z]way", "What a way to go"))
#We can define more ranges like upper case A to upper case Z for all upper case letters or 0 to 9 for all digits. We can combine as many ranges and symbols as we want, like this.
#print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))

#code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.
def check_punctuation (text):
    result = re.search(r"[,.:;?!]", text)
    return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#search pattern that looks for any characters that's not a letter.
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
#an expression that matches either the word cat or the word dog
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

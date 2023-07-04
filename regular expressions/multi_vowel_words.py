#! python

# The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u).
import re
def multi_vowel_words(text):
    # \w*: Matches zero or more word characters (alphanumeric characters and underscores) before and after the consecutive vowels. This allows for any number of non-vowel characters to appear before or after the consecutive vowels within a word.
    # [aeiou]{3,}: Matches 3 or more consecutive vowels (a, e, i, o, u). The {3,} quantifier ensures that there are at least 3 occurrences of the vowel characters in a row.
    # \w*: Similar to the first \w*, matches zero or more word characters after the consecutive vowels.
  pattern = r"\w*[aeiou]{3}\w*"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []
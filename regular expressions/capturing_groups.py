#! python

import re

"""
# \w will match letters, numbers, and underscores.
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")

print(result)
print(result.groups())
print(result[1])
print(result[2])
print(f"{result[2]} {result[1]}")
"""

def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    
    if result is None:
        return name
    return f"{result[2]} {result[1]}"
    """
    result = re.search(r"^(\w*), (\w*)(?: (\w\.|\w+))?$", name)
    
    if result is None:
        return name
    return f"{result[2]} {result[3]} {result[1]}" if result[3] else f"{result[2]} {result[1]}" """

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))
#! python
import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# \[ matches the opening square bracket character "[".
# (\d+) captures one or more digits.
#  The parentheses () are used to create a capturing group, and \d represents any digit character.
# \] matches the closing square bracket character "]".
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

#  Let's try our expression on a different string and check that it really works, no matter what the rest of the text is.
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

# what if our string didn't actually have a block of numbers between the square brackets?
# result =  re.search(regex, "99 elephants in a [cage]")
# print(result[1])

#  defining a function called extract_pid.
def extract_pid(log_line):
    # regex = r"\[(\d+)\]"
    regex = r"\[(\d+)\].*?([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return f"{result[1]} ({result[2]})"

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

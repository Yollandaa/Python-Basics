# Regex -> Regular Expressions
# Pattern match in a string

numbers = """38795475, 4985048584, 098305843, 987077540545, 9348584854545
            38795475, 4985048584, 098305843, 987077540545, 9348584854545"""
# \d\d\d: Anything from 0-9
# \D: Anything that is not a digit
# .: Anything will match
# \s: Anything that is a space
# ..: Anything that is not a space
# \.: Exactly 
# [abc]d: Anything that is a, b, or c, and it should have d after
# [^abcs]: Anything that is not a, b, or c
# [a-z]: Anything that is a-z ( from a to z)
# \w ==  [A-Za-z0-9_]: Anything that is a-z, 0-9, or _ (Alphanumeric)
# \W: Anything that is not a-z, 0-9, or _ 
# {w}: Exactly w times (repetition)
# n+ : One or more
# *: Zero or more times
# ab?c:  will match either the strings "abc" or "ac" because the b is considered optional.
#  [^...]: Anything that is not ...
#  ^hat$: Matches the string "hat" at the beginning and end of the string.
# ^success: Matches the string "success" at the beginning of the string.
# success$: Matches the string "success" at the end of the string.
# ^(IMG\d+\.png)$: Matches the string "IMG123.png" at the beginning of the string.
# .*x.* : A greedy approach takes anything with x inbetween and anything after
# .*x.*? : A non-greedy approach takes anything with x inbetween and anything after




# Tasks:
# 1. ...\.
# 2. [cmf]can: either start with c,m, or f, a followed by can
# 3. [^b]og: does not start with b, and ends in og
# 4. [A-Z]: Starts with a capital letter
# 5. waz{3,6}up: words starting with waz, with 3-6 letters in between that are z, ending with up.
# 6. fu[nz]{2}y: words starting with fu, with 2 letters in between that are n or z, ending with y
# 7. aa+b*c+: starts with 2 or more a's, followed by 0 or more b's, followed by 1 or more c's
# 8. \d\.\s+abc: starts with a digit, followed by a dot, with 1 or more spaces, followed by abc
# 9. ^Mission: Matches a string that starts with the word "Mission"
# 10. ^(file_\w+)\.pdf$: Matches a string that starts with the word "file_" followed by a word, ends with .pdf
# 11. ^(\w{3}\s(\d{4}))$: Matches a string that starts with 3 letters, followed by a space, followed by 4 digits, then another 4 digits in a subgroup
# 12. (\d{4})x(\d+): Capture the 4 digits, followed by an x, followed by 1 or more digits: get the numbers between the x
# 13. I love (cats|dogs): Matches the string "I love cats" or "I love dogs"

# Apply this in python

import re
quote = "To be or not to be"
is_be = re.search(r'be$', quote)
output = "Present" if is_be else "Not present"
print(is_be, type(is_be))
print(output)

print()

quote1 = "funny funy funnnny fuzzy"
find_be = re.findall(r'fu[nz]{2}y', quote1)
print(find_be)

print()

# r is raw string, we use it so we don't have to escape characters: no slash needed
text = "This \\ that \\ those"
matches = re.findall("\\\\", text)
matches_r = re.findall(r"\\", text)
print(matches)
print(matches_r)

tweet = "Spoiler: This movie is great, but the spoiler was unexpected. Avoid sharing spoilers!"
# *****
censor_tweet = re.sub(r"(spoiler|but)", "*" * 7 , tweet, flags=re.IGNORECASE)
print(censor_tweet)

print()
# Can get the subdomain using "\1" or "\2"
list_website = "facebook.com, google.com, twitter.in, amazon.com"
result = re.sub(r'(\w+)(\.com), ' , r'\1.subdomain\2 ' , list_website)
print(result)

print()

names = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Evans", "JamesCodey"]
# Switch the first and last name
# Expected output: ["Doe, John", "Smith, Jane", "Johnson, Alice", "Evans, Chris"]
switched_names = [re.sub(r'(\w+)\s+(\w+)', r'\2, \1', name) for name in names]
print(switched_names)
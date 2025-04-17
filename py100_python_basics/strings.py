# - - - - - - - - - - - - - -
# Length
# Determine the length of the string

# text = "These aren't the droids you're looking for."
# print(len(text))

# - - - - - - - - - - - - - -
# ALL CAPS
# Convert the string 'confetti floating everywhere' to all upper case.

# text = 'confetti floating everywhere'

# print(text.upper())

# - - - - - - - - - - - - - -
# Ignoring Case
# Using the following code, compare the value of name with the 
# string 'RoGeR' while ignoring the case of both strings. 
# Print true if the values are the same; print false if 
# they aren't. Next, perform a case-insensitive comparison 
# between the value of name and the string 'DAVE'.

# name = 'Roger'
# name2 = 'RoGeR'
# name3 = 'DAVE'

# print(name.casefold() == name2.casefold())
# print(name.casefold() == name3.casefold())

# - - - - - - - - - - - - - -
# Multiline String

# How can you assign the following rhyme to a single variable 
# while preserving the line break?

# one way:

# rhyme = 'A pirate I was meant to be! \nTrim the sails and roam the sea!'

# print(rhyme)

# another way:

# rhyme = '''A pirate I was meant to be!
# Trim the sails and roam the sea!'''

# print(rhyme)

# - - - - - - - - - - - - - -
# Contains Character

# Write code that checks whether the string char_sequence 
# contains the character x.

# char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

# print('x' in char_sequence)

# - - - - - - - - - - - - - -
# Is Empty?
# Write a function that checks whether a string is empty or not.

# def is_empty(text):
#     return not text

# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True

# - - - - - - - - - - - - - -
# Is Empty or Blank?
# Write an is_empty_or_blank function to determine whether 
# a string is either empty or consists entirely of spaces. 

# def is_empty_or_blank(text):
#     text_stripped = text.strip()
#     return not text_stripped

# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True

# - - - - - - - - - - - - - -
# Capitalize Words
# Write code that capitalizes the words in the string 
# 'launch school tech & talk', so that you get the string 
# 'Launch School Tech & Talk'.

# text = 'launch school tech & talk'
# print(text.title())

# - - - - - - - - - - - - - -
# Check Prefix
# Write a function that checks whether a string starts 
# with a specific prefix.

# def starts_with(text, substring):
#     return text.startswith(substring)

# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

# - - - - - - - - - - - - - -
# Count Substrings
# Write a function that counts the number of occurrences 
# of a substring in a string.

def count_substrings(text, substring):
    return text.count(substring)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0
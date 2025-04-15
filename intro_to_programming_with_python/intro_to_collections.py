# 1. If you have a list named people, how can you determine 
# the number of entries in that list?

# Solution:
# len(people)

# 2. Can you write some code to change the value 'bye' in 
# the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

# Solution:

# tuples are immutable so convert to list, change list element at index 2,
# convert back to tuple

# one way
# stuff_list = list(stuff)
# stuff_list[2] = 'goodbye'
# stuff = tuple(stuff_list)
# print(stuff)

# another way

# print(stuff[:2] + ('goodbye',) + (stuff[3],))

#- - - - - - - - - - - - - - 
# 3. Identify at least 2 differences between lists and tuples. 
# Identify at least 2 ways that lists and tuples are similar.

# Solution:

# Differences between lists and tuples: 
# 1. Lists are mutable and tuples are immutable
# 2. Lists are signified using square brackets `[]` and
# tuples use `()`

# Similarities between lists and tuples:
# 1. Lists and tuples are ordered sequences that can be indexed, 
# sliced, and iterated over
# 2. Lists are tuples are heterogeneous collections

# - - - - - - - - - - - - - -
# 4. Why can we treat strings as sequences?

# Solution: 
# strings can be treated as sequences because they are ordered
# and can be indexed, sliced, and iterated over.

# - - - - - - - - - - - - - -
# 5. How do the set types differ from the sequence types?

# Solution:
# Sets are unordered collections, while sequences are ordered and 
# can be indexed and iterated over

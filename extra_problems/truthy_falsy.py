# print(True and False or True)


# Solution:
# This will print: True

# The `and` expression takes precedence so the first subexpression
# evaluated is `True and False` which returns `False` because the `and`
# operator returns the first falsy value or the last value if all are 
# truthy. In this case `True` is truthy so it returns `False`. The 
# expression becomes `print(True or True)` which evaluates to `True`
# because the `or` operator returns the first truthy value.

# - - - - - - - - - - - - - -
# print('a' or 0 and True)

# Solution:
# This will print: a
 
# Because `and` takes precedence over `or`, this expression is the same as:
# print('a' or (0 and True)) with the parens setting off the first subexpression
# evaluated. `0 and True` This returns `0` because `0` is falsy, and the `and` 
# operator returns the first falsy value or last value if all are truthy. 
# The expression then becomes `print('a' or 0)` which prints 'a' because 
# `a` is truthy, and `or` returns the first truthy value or last value if 
# all are falsy.

# - - - - - - - - - - - - - -
#print('' or None and (5 > 3) or 0)


# This will print: 0
# Because `and` takes precedence over `or`, this expression is the same as:
# ('' or (None and (5 > 3)) or 0) with the parens setting off the first 
# subexpression evaluated: `None and (5 > 3)`. Because 5 > 3 is `True`, this
# becomes `None and True`, which returns `None` because `and` returns the first
# falsy value. The expression is now: `('' or None or 0)`. An empty string `''`, 
# `None`, and `0` are all falsy. The `or` operator returns the first truthy 
# value or the last value if all are falsy, which is the case in this example.

# - - - - - - - - - - - - - -
# print(bool('False') and not bool('')) or bool(0) and bool([])

# Solution: 
# This will print: True
# bool('False') returns `True` because it's a non-empty string; it doesn't
# matter if the string is 'False', it's evaluated as a non-empty string.
# bool('') returns `False` because it's an empty string. This is negated by
# the `not` operator, which becomes `True`. bool(0) and bool([]) both return 
# `False`. Substituting these values, this expression becomes:
# print(True and True or False and False). `and` takes precedence over `or`
# so this is evaluated as: `(True and True) or (False and False)`
# which is `True or False` because `True and True` is `True` and 
# `False and False` is `False`. `True or False` is `True` because
# `or` returns the first truthy value.

# - - - - - - - - - - - - - -
#print('' or 'Python' and 0)

# This will print: 0

# ('Python' and 0) returns 0
# ('' or 0) returns 0

# - - - - - - - - - - - - -

#print(bool('') or bool(0) or bool([]))


# This will print: False
# empty string (''), (0), and empty list ([]) are all False
# So this will be False

# - - - - - - - - - - - - - -

# print(not False and not True)

# This will print: `False`
# `not False` returns `True` and `not True` returns `False`
# so this expression becomes `True and False`. This returns `False` 
# because `and` returns the first falsy value or last value if all are truthy.

# - - - - - - - - - - - - - -

#print(5 > 3 and 'hello' != 'world')

# This will print: True
# The comparison operators `>` and `!=` take precedence over `and`
# So this expression is equivalent to `(5 > 3) and ('hello' != 'world')`
# This becomes `True and True`  because `5 > 3` is `True` and
# `'hello' != 'world'` is `True`
# `True and True` is `True`

# - - - - - - - - - - - - - -
# print('abc' > 'abd' or True)

# This will print:  True

# The `>` takes precedence so this is evaluated as `(('abc' > 'abd') or True)`
# 'abc' > 'abd' is False because Python compares each character lexicographically
# (according to the order in the ASCII table) from left to right. Each string 
# contains 'a' and 'b', so 'c' and 'd' are compared. 'c' is less than 'd' 
# according to the ASCII table, so this is `False`. The expression becomes
# `False or True` which returns `True` because the `or` operator returns the 
# first truthy value or last value if all are falsy. 

# - - - - - - - - - - - - - -
# x = 10
# print(x > 5 and x < 15 or x == 20)

# Solution:
# This expression is evaluated as
# print(10 > 5 and 10 < 15 or 10 == 20)
# The `>`, `<`, and `==` operators take precedence over
# `and` and `or` so this becomes
# `True and True or False`. `True and True` is `True`.
# `True or False` is `True` because `or` prints the first
# truthy value
# - - - - - - - - - - - - - -
#print(bool([]) == False and bool('False') == True)

# This will print: True

# `bool([])` is `False` because empty lists are falsy. 
# `bool('False)` is `True` because it's a non-empty string
# even if the string is 'False'. So `False == False` is `True`
# and `True == True` is `True`
# - - - - - - - - - - - - - -

#print((False or []) and ('B' < 'b') or None)

# This will print: `None`
# `or` return first truthy value or last value if all are falsy so
# `False or []` returns `[]`. The next subexpression returns `True`
# because uppercase characters are considered less than lowercase characters.
# So the expression becomes: `[]` and `True` or `None`
# `and` has higher precedence than `or` so this evaluates from 
# left to right. `and` returns first falsy value then short circuits
# so expression becomes `[] or None`. `or` returns first truthy value or
# last value so `None`

# - - - - - - - - - - - - - -
# a = 0
# b = 1
# print(a or b and not a)

# (0 or 1 and not 0)
# In order of precedence, python evaluates `not`, `and`, `or`
# Starting with `not 0`, `not` always returns a boolean 
# `True` or `false`. Because `0` is falsy, `not 0` returns `True`
# So expression becomes (0 or (1 and True)). `1 and True` returns
# `True` because `and` returns first falsy value or last value if
# all are truthy. Expression then becomes `0 or True` which returns
# `True` because `or` returns first truthy value or last value if
# all are falsy 

# - - - - - - - - - - - - - -
#print('' and None or [] and 'python' or 0)

# This prints: 0
# `and` takes precedence over `or` so going from left to right, first
# subexpression `'' and None` returns `''` because `and` returns first
# falsy value. Expression becomes: ('' or [] and 'python' or 0). 
# The `and` subexpression then evalues: `[] and 'python'` which returns
# [] because it's falsy, so the expression becomes: ('' or [] or 0).
# `or` returns the first truthy value or the last value if all are falsy
# so this returns 0

# - - - - - - - - - - - - - - 
#print(not (0 or '') and (True and 'hello'))

# This prints: 'hello'
# Evaluating subexpressions in parentheses first: `0 or ''` returns
# `''` because `or` returns first truthy value or last value if all are falsy.
# `True and 'hello` returns 'hello' because `and` returns first falsy value or
# last value if all aare truthy. So this expression becomes:
# (not ('') and ('hello')). `''` is falsy which `not` negates so `True and 'hello'
# Both values are truthy so this returns 'hello'

# - - - - - - - - - - - - - -

#print(bool(0) or bool('') or not bool([1, 2]))

# This prints: False
# `0` and empty list `''` are both falsy so `bool(0)` and
# `bool('')` return `False`. A non-empty list is truthy so
# `bool([1, 2])` returns `True`. So this expression becomes:
# (False or False or not True) which is (False or False or False).
# `or` returns the first truthy value or last value if all are falsy

# - - - - - - - - - - - - - -
#print('a' in 'abc' and 'x' not in 'xyz' or 5 >= 5)


# This will print: True
# order of precedence:  in/not in, >=, and, then or
# So this is evaluated as 
# (('a' in 'abc) and ('x' not in 'xyz') or (5 >= 5))
# which becomes (True and False or True) then
# (False or True) which is True
 
# # - - - - - - - - - - - - - -
# a = []
# b = a
# print(a is b and a == b or a is not [])


# This will print: True
# In order of precedence, `is` and `is not` evaluated first,
# followed by `==`, then `and`, finally `or`
# Expression evaluated as:
# 1. `a is b` evaluates to True because `is` checks for object
#   identify and `a` and `b` both point to same empty list object
#   in memory.
# 2. `a is not []` evaluates to `True` because `is not` checks for 
#   object equality, and `a` points to a different empty list in 
#   memory as the literal `[]` in the subexpression
# 3. `a == b` evaluates to `True` because `==` checks for value
#   equality and both `a` and `b` are empty lists
# So the expression becomes:  True and True or True
# 4. `True and True` evaluates to `True` because `and` returns
#   last value if none are falsy.
# 5. `True or True` evaluates to `True` because `or` returns
#   first truthy value



# - - - - - - - - - - - - - -
#print(len('python') > 5 and 'on' in 'python' or 4 < 3)

# This prints True
# Order of precedence:  `in`, comparison operators `>` and `<`,
#  followed by `and` then `or`
# 1. 'on' in 'python' is True
# 2. len('python') is 6, 6 > 5 is True and 4 < 3 is False
# So this is evaluated as: True and True or False
# 3. `True and True` returns True
# 4. `True or False` returns True


# - - - - - - - - - - - - - -

#print(None and print('hello') or print('world'))
# Subexpression `None and print('hello') short circuits because `and`
# returns first falsy value. 
# None or print('world') evaluates to print('world') because 'or' 
# returns first truthy value or last value if all are falsy
# So what will print(print('world')) do? This is a nested function.

# The inner `print` function call outputs 'world', then it returns 'None'. 
# `None` is then passed as an argument to the outer `print` function invocation.



# - - - - - - - - - - - - - -
print('' or [] and False or None is None and not ([] or {}))

# This prints:  True
# Empty string '', empty list [], False, None, and empty dictionaries {} 
# are all falsy.

# In order of precedence, the is operator is evaluated first, then not, 
# and, followed by or. Based on this, the expression is evaluated 
# as if the following subexpressions are in parentheses:
# '' or ([] and False) or (None is None) and not ([] or {})

# [] and False evaluates to [] because and returns the first falsy value.
# None is None evaluates to True because is checks for object equality and 
# there is only one None object in python.
# [] or {} evaluates to {} because or returns the last value if none of 
# the values are truthy, so then not {} evaluates to True because not
# negates the falsy empty list
# So now python evaluates the expression as: '' or [] or True and True. 
# Because and has precedence over or, it evaluates the subexpression True and True
# which is True
#  The expression is now evaluated as '' or [] or True which 
# is True because or returns the first truthy value.







# [] and False or True and not {}
# [] or True and True
# True and True 

# - - - - - - - - - - - - - -
# a = [1, 2]
# b = [1, 2]
# print(a is not b and a == b or len(a) > 3 and not a)

# `a is not b` is True because a and b do not point to the same objects
# `a == b` is True because a and b have the same value
# `len(a) > 3` is False because len(a) is 2, which is not > 3 
# not a is False because a is truthy
# so this becomes
# True and True or False and False
# True or False and False
# True or False
# True




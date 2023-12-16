"""
Lists are equivalent of arrays, flexible about type. Insertion/deletion can be costly
due to shifting elements, and also insertion/deletion at the end of a list can be costly
if preallocated memory is full.

Dictionaries are equivalent of hash tables. time complexity of O(1). Unordered collection of
data values stored like a map in key:value pairs.

Tuple is a collection of Python objects similar to a list, but immutable.
"""

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict.get(1))

# Dictionary comprehension

myDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(myDict)

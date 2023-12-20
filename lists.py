"""
Lists are equivalent of arrays, flexible about type. Insertion/deletion can be costly
due to shifting elements, and also insertion/deletion at the end of a list can be costly
if preallocated memory is full.

Dictionaries are equivalent of hash tables. time complexity of O(1). Unordered collection of
data values stored like a map in key:value pairs.

Tuple is a collection of Python objects similar to a list, but immutable and can also contain
elements of different types

Sets are unordered collections of mutable data with no duplicates. Most commonly used for
membership testing and eliminating duplicates. Uses hashing for O(1) insertion, deletion,
traversal. If multiple values are present at same index position, then the value is appended
to that index position to form a Linked List.
"""

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mid = len(sample) // 2  # // will round, useful for midpoint
left = sample[:mid]
right = sample[mid + 1:]
midrange = sample[1:8]
print(mid)
print(sample[mid])
print(left)
print(right)
print(midrange)

# List comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:", list_using_comp)


Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print(Dict.get(1))

# Dictionary comprehension

myDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(myDict)

list1 = [1, 2, 3, 4, 5]
Tuple = tuple(list1)
print(Tuple)

Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print(Set)

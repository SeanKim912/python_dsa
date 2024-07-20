'''
Another type of Python container which encapsulates many dictionaries into one unit. Member of the
"collections" module.
'''

from collections import ChainMap;
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

c = ChainMap(d1, d2, d3)

print(c)
print(c.keys())
print(c.values())
print(c.maps) # Prints as a list

d4 = {'g': 7, 'h': 8}
c.new_child(d4) # Adds new dictionary to beginning of ChanMap
print(c)
print(reversed(c.maps)) # Reverses relative ordering of dictionaries

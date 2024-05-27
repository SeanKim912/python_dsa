name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Original names:", name_list)

name_list.sort()
print("Sorted names:", name_list)

name_list.sort(key = lambda name: name.split()[1])
print("Sorted by last names:", name_list)

# Sort and sorted both have optional parameters, "key" which lets you sort by criteria, and reversed, which is a boolean that indicates ascending or descending order.

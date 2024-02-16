nums = [3, 4, 7, 9, 1, 2, 8, 6, 5, 0]
nums.sort()
print(nums)

print(type(nums))

nums.append(10) # append() only adds one element to a list
print(nums)

nums.extend([11, 12, 13]) # extend() adds multiple elements to a list
print(nums)

print(nums.index(7)) # returns the index of the first occurrence of a value

print(max(nums)) # returns the maximum value in a list
print(min(nums)) # returns the minimum value in a list
print(len(nums)) # returns the length of a list

garbage = ["trash", "rubbish", "litter", "debris", "waste"]

trash = garbage.count("trash")
print(trash) # returns the number of times a value occurs in a list
garbage.insert(0, "turd") # inserts an element at a specific index
print(garbage)

garbage.pop() # removes the last element from a list
garbage.pop(3) # removes the element at a specific index

garbage.remove("rubbish") # removes the first occurrence of a value from a list
print(garbage)

garbage.reverse() # reverses the order of elements in a list
print(garbage)
garbage_copy = garbage.copy() # creates a copy of a list
print(garbage_copy)

garbage.clear() # removes all elements from a list
print(garbage)

def filter_func(num):
    if num % 2 == 0:
        return num
    else:
        return

filtered_output = filter(filter_func, nums)
print(list(filtered_output))

x = range(3, 11, 2)
print(x)
print(list(x))

y = range(10)
print(y)

print(abs(-3)) # returns the absolute value of a number

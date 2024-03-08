file = open("test_text.txt") # Must open a file before you can perform any operations on it.
contents = file.read()
print(contents)

file = open("test_text.txt", "w") # Must open file in write mode
file.write("This is some text I added \n") # New content will replace existing content!

file.close()

# Using with ... open method closes file automatically
with open("test_text.txt", "a") as file2: # 'a' for append mode
    file2.writelines(["apples\n", "oranges\n", "bananas\n"]) # Right list of lines

with open("test_text.txt", "r") as file3:
    read_content = file3.readline() # Read one line each time it's called, or a specified number of bytes
    read_content2 = file3.readlines(3) # Returns all lines in a list (default) or a specified #
    print(read_content)
    print(read_content2)

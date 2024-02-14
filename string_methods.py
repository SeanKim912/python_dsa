# 1. Slicing
s = "Hello, World!"
print("1A", s[2:5])
print("1B", s[:5])
print("1C", s[2:])
print("1D", s[-5:-2])
print("1E", s[2:20]) # Does not throw an error, simply prints up to the end of the string

# 2. strip() method removes any whitespace from the beginning or the end if parameter is None or not specified, or a specified string from the beginning or the end of the string
str = "   Hello, World!   "
str2 = "***Hello, World!***"
print("2A", str.strip())
print("2B", str.lstrip())
print("2C", str.rstrip())
print("2D", str2.strip("*"))
print("2E", str2.lstrip("*"))

# 3. replace() method replaces a string with another string
print("3A", s.replace("H", "J")) # Empty string will simply remove the character

# 4. re.sub() method uses regular expressions to replace a string
import re
s4 = "string    methods in python"
s4a = re.sub("\s+" , "-", s4)
print("4A", s4a)

# 5. split() method splits the string into substrings if it finds instances of the separator
print("5A", s.split(","))

# 6. join() method takes all items in an iterable and joins them into one string
list_of_strings = ['string', 'methods', 'in', 'python']
s5 = ' '.join(list_of_strings)
print("6A", s5)

#7. upper(), lower(), capitalize() methods
print("7A", s.upper())
print("7B", s.lower())
print("7C", s.capitalize())

#8. isupper(), islower() methods
print("8A", s.isupper())

#9. isnumeric(), isalpha(), isalnum() methods
print("9A", s.isnumeric())
print("9B", s.isalpha())
print("9C", s.isalnum())

#10. count() method returns the number of times a specified value appears in the string
print("10A", s.count("l"))

#11. find() method finds the first occurrence of the specified value
print("11A", s.find("e"))

#12. rfind() method finds the last occurrence of the specified value
print("12A", s.rfind("l"))

#13. startswith() method returns True if the string starts with the specified value
print("13A", s.startswith("H"))

#14. endswith() method returns True if the string ends with the specified value
print("14A", s.endswith("!"))

#15. f-strings (formatted string literals)
name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")

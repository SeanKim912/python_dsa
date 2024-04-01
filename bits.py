x = 0b00100
y = 0b00100
x = x >> 1 # Shift all bits to the right by n amount
y = y << 1 # Shift all bits to the left by n amount
print(x)
print(y)

# The code below is for counting bits (how many 1's)
def countBits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1
    return count

print(countBits(23))

'''
    23 is 10111 in binary. "n & 1" (&, NOT 'and') is the same as comparing 10111 to 00001 digit by digit. If both digits are 1, increase the count,
    and shift to the right, so then you compare 1011 to 0001. When you've shifted n all the way to 0, you should get a count of 4 (4 bits that are 1 in 10111).
'''

a = 1 & 1 # AND
b = 1 | 0 # OR
c = 1 ^ 1 # XOR
d = ~c # NOT (negation)

print(a)
print(b)
print(c)
print(d)

print(bin(55))
print(int(0b10111))

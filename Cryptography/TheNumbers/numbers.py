# Harris Ransom
# PicoCTF - The Numbers
# Category: Cryptography

# Given values
numbers = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

# Convert numbers to ASCII
flag = ''.join([chr(x + 64) if type(x) == int else x for x in numbers])
print(flag)
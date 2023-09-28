letters=["d","a","b","c","e"]
print("Letters:",letters)

print("Index of a:",letters.index("a"))

# print("Index of f:",letters.index("f"))
# ValueError: 'f' is not in list

# Way 1 " To make sure program doesn't break if element is not found

if 'f' in letters:
    print("Index of f:",letters.index("f"))
else:
    print("f is not in letters list")

# Way 2: To make sure program doesn't break if element is not found

count=letters.count("d")

if count>0:
    print("Index of d:",letters.index("d"))

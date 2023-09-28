letters=["a","b","c","e"]

print("Original",letters)

# Add the elements

letters.append("f")
print("Append",letters)

# Insert Elements

letters.insert(3,"d")
print("Insert:",letters)

# Remove
removed=letters.pop(0)
print("Removed Value from List",removed)
print("Popped",letters)

letters.remove("e")
print("Removed",letters)

del letters[1]
print("After del:",letters)

numbers=list(range(100,110))
print("N:",numbers)

del numbers[4:6]
print("After Del:",numbers)

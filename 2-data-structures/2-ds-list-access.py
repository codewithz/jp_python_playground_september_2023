letters=["a","b","c","d","e"]

print(letters)

# Access the first element

print("First Element",letters[0])

print("Last Element",letters[-1])

# Access in Ranges

print(letters[0:2])
print(letters[:3])
print(letters[2:])

# Clone

letters_clone=letters[:]
print(letters_clone)

# Steppers

numbers=list(range(1,21))
print(numbers)

print(numbers[::2])
print(numbers[::1])
print(numbers[::-1])
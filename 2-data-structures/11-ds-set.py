# Set --> NO DUPLICATES | UNORDERED

#  {}

numbers=[1,2,3,4,6,7,4,4,5,5]
# numbers=[1000,132,1453,4523,61251,7534352,455324234,4132536,54536524,52534524]

print("List:",numbers)

first=set(numbers)
print("Set:",first)

first={*numbers}
print("Set with list:",first)

second={1,4,5}

print(40*"-")
print("First",first)
print("Second",second)

# Add and Remove
print(40*"-")
second.add(6)
print("Second",second)

print(40*"-")
second.add(6)
print("Second",second)

print(40*"-")
second.remove(4)
print("Second",second)

# print(40*"-")
# second.remove(4)
# print("Second",second)

print(40*"-")
second.discard(4)
print("Second",second)


print("--------------- Set Operations --------------------")
print("First:",first)
print("Second:",second)

print("Union:",first.union(second))

print("Intersection:",first.intersection(second))

print("Difference:",first.difference(second))
print("Difference:",second.difference(first))

print("Symmetric Difference",first.symmetric_difference(second))
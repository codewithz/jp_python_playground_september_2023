# Tuples are read only list
#  ()

# Ways to define a Tuple

point=(1,2)
print(type(point))
print(point)

point=1,
print(type(point))
print(point)

point=1,2
print(type(point))
print(point)

point=(1,2)+(3,4)
print(type(point))
print(point)

point=(1,2)*3
print(type(point))
print(point)

point=("JP",)*3
print(type(point))
print(point)

# Accessing Elements in Tuple

print(40*"-")

point=(1,2,3)

print(point)
print("Index[1]:",point[1])
print("Range",point[0:])
print("Range",point[0:2])

x,y,z=point

print("x:",x)
print("y:",y)
print("z:",z)

if 10 in point:
    print("10 is there in tuple")
else:
    print("10 is not in tuple")

print(40*"-")
#
# point[1]=30
# TypeError: 'tuple' object does not support item assignment
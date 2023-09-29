# Dictionary
# Key-Value Pairs
#  {key:value,key:value}
# Contact Book   Name --> Contact Number

print("-"*40)
point={"x":1,"y":2}
print(point)
print(type(point))

print("-"*40)
point=dict(x=1,y=2)
print(point)
print(type(point))

print("-"*40)

point["x"]=10
point["y"]=20
point["z"]=30

print(point)
print(type(point))

print("_"*20,"Accessing the Data","_"*20)

print("X:",point.get("x"))
print("X:",point["x"])
print("A:",point.get("a"))
print("A:",point.get("a",0))

# How do we iterate through a Dictionary

print(40*"-")

for something in point:
    print(something)

print(40*"-")

for key in point:
    print(key)

print(40*"-")

for item in point.items():
    print(item)

print(40*"-")

for key,value in point.items():
    print(key,"--",value)

key_list=point.keys()
value_list=point.values()

print("Keys:",key_list)
print("Values:",value_list)

for key in key_list:
    print(key)
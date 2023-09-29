print(20*"-","Complex Object Sorting",20*"-")

cart=[("Bread",15,2),("Jam",3,1),("Butter",7,3)]

print("Cart:",cart)

# def key_for_sort_cart(item):
#     return item[1];
#
# sorting_key= lambda item:item[1]

cart.sort(key=lambda item:item[1])
print("Cart:",cart)

# -----------------------------------------------
print(40*"-")

numbers=[1,2,3,4,5,6,7,8,9,10]

squares=[]

for number in numbers:
    squares.append(number*number)

print("Numbers:",numbers)
print("Squares:",squares)

squares_list=list(map(lambda number:pow(number,2),numbers))

print("Numbers:",numbers)
print("Squares using Lambda:",squares_list)



print(40*"-")
cart=[("Bread",15,2),("Jam",3,1),("Butter",7,3)]
prices=[]

for name,price,qty in cart:
    prices.append(price)

print("Prices:",prices)

prices_list=list(map(lambda item:item[1],cart))
print("Prices using Lambda:",prices_list)


print(40*"-")
# Filter Function

# filtered_cart=[]
#
# for item in cart:
#     name,price,qty=item
#     if(price>5):
#         filtered_cart.append(item)
#
# print("Filtered Items",filtered_cart)

filtered_cart=list(filter(lambda item:item[1]>5,cart))
print("Filtered Items using Lambda",filtered_cart)

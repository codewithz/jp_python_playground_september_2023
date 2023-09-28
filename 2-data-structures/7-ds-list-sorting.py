numbers=[3,51,2,45,8,67]
print("O:",numbers)

numbers.sort()
print("S:",numbers)
print("O:",numbers)

numbers.sort(reverse=True)
print("RS:",numbers)

print("-"*40)

# ----------------------------------------------------------

other_numbers=[43,65,34,0,23,89]
print("O:",other_numbers)

sorted_list=sorted(other_numbers)
print("S:",sorted_list)
print("O:",other_numbers)

reverse_sorted=sorted(other_numbers,reverse=True)
print("RS:",reverse_sorted)
print("O:",other_numbers)

# -------------------------------------------------------

print(20*"-","Complex Object Sorting",20*"-")

cart=[("Bread",15,2),("Butter",7,3),("Jam",3,1)]

print("Cart:",cart)

def key_for_sort_cart(item):
    return item[1];

cart.sort(key=key_for_sort_cart)
print("Cart:",cart)

def key_for_qty_sort_cart(item):
    return item[2]

cart.sort(key=key_for_qty_sort_cart)
print("Cart:",cart)

def key_for_total_price_sort_cart(item):
    return item[1]*item[2]


cart.sort(key=key_for_total_price_sort_cart,reverse=True)
print("Cart  --  :",cart)
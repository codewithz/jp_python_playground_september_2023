cart=[("Bread",15,2),("Jam",3,1),("Butter",7,3)]
print("Cart:",cart)

prices=list(map(lambda item:item[1],cart))
print("Prices:",prices)

# List Comprehension
# Map
# [expression for item in items]

prices=[item[1] for item in cart]
print("Prices LC:",prices)

qtys=[item[2] for item in cart]
print("Qty's LC",qtys)

# Filter
# [expression for item in items if condition]

filtered_cart=[item for item in cart if item[1]>5]
print("Filtered Cart:",filtered_cart)


names=["Tom","Alex","Ricky","Leanord","Sheldon"]

len_list=[len(name) for name in names]
print("Len Items",len_list)

# ------------------------------------------------------------------------------------------
employees=[
    (1,"Tom","IT",30000),
    (2,"Alex","Accounts",33000),
    (3,"Mike","Finance",43000),
    (4,"John","HR",39000),
    (5,"Penny","IT",45000)
]

#  Q1 -- Find the list of departments in employees list
# Q2 -- find those employees whose salary is greater than 32k and work in IT

departments=[employee[2] for employee in employees]
print("Department:",departments)
departments=set(departments)
print("Departments",departments)

# ----------------Q2---------------------------

filtered_list=[employee for employee in employees if (employee[3]>32000 and employee[2]=='IT')]
print(filtered_list)
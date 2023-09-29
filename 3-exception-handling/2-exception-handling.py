try:
    age=int(input("Enter Age:"))
    print(f"Age is {age}")
except ValueError as ex:
    print("You entered an invalid age")
    print(ex)
    print(type(ex))
else:
    print("Else after try executes when there is no exception")




print()
print()

print("Execution continues............")
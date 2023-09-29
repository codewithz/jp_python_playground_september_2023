try:
    file=open("test.txt")
    print("Is file closed? :",file.closed)
    age=int(input("Enter Age:"))
    xfactor=10/age
    print(f"Age is {age}, XFactor is {xfactor}")

except ValueError as ex:
    print("VE : Invalid Age entered")
except ZeroDivisionError as ex:
    print("ZDE: You seems to be entered zero as age")
except Exception as ex:
    print("Some other exception occurred")
    print("Reason:",ex)
else:
    print("No exception have occurred")
finally:
    print("This block executes in all conditions [Exception occurred or not]")
    file.close()
    print("Is file closed? :",file.closed)

print()
print()
print("Execution continues.....")
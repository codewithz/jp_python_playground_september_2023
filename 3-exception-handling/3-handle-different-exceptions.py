import  traceback
try:
    age=int(input("Enter Age:"))
    xfactor=10/age
    print(f"Age is {age}, XFactor is {xfactor}")
    numbers=[123,456]
    print(numbers[3])

except ValueError as ex:
    print("VE : Invalid Age entered")
except ZeroDivisionError as ex:
    print("ZDE: You seems to be entered zero as age")
except Exception as ex:
    print("Some other exception occurred")
    traceback.print_exc()
    print("Reason:",ex)






print()
print()
print("Execution continues.....")
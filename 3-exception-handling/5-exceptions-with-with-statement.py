try:
    with open("test.txt") as source,open("names.txt") as target:
        x=10/1
        print(f"Value of x is {x}")
        print("Status of file used under source | Is file closed?:",source.closed)
        print("Status of file used under target | Is file closed?:",target.closed)
        print(20*"-","With Block ends here",20*"-")

    print("Status of file used under source | Is file closed?:",source.closed)
    print("Status of file used under target | Is file closed?:",target.closed)
except Exception as ex:
    print("Some Exception Occurred")




print()
print()
print("Execution continues.....")
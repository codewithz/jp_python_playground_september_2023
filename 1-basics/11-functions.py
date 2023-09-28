print(20*"-","Normal Function",20*"-")

def greet():
    print("Hi There")
    print("Welcome Aboard")
# --------------------------------------------------------
greet();
# --------------------------------------------------------

def add_two_numbers(number1,number2):
    print(number1,"+",number2,"=",(number1+number2))


add_two_numbers(10,20)
add_two_numbers(11,22)
add_two_numbers(54,32)
add_two_numbers(12,55)

print(20*"-","Function with return type",20*"-")

# Types of Functions
# 1. Perform a task
# 2. Do some processing and return a value

# 1. Perform a Task

def greet(name):
    print("Hi ",name)


greet("Tom")


# 2. Do some processing and return a value

def get_greeeting(name):
    return "Hi "+name;

message=get_greeeting("Alex")

# Send this in an email
# Store this in DB
# Store it in a file
# Send it over a network
# Print in log

print(message)

# ----------- Keyword Arguments---------------
print(20*"-","Keyword Arguments",20*"-")
import math



def increment_after_factorial(number,by):
    factorialed_number=math.factorial(number)
    add_to_factorialed_number=factorialed_number+by
    return add_to_factorialed_number;
# -------------------------------------------------------------
result=increment_after_factorial(4,2)
print(result)
result=increment_after_factorial(5,1)
print(result)

result=increment_after_factorial(by=3,number=4)
print(result)


# ----------- Default Arguments---------------
print(20*"-","Default Arguments",20*"-")

def increment(number,by=1):
    return  number+by
# ---------------------------------------------------------------

result=increment(45)
print(result)

result=increment(6,3)
print(result)

# ----------- Varying Arguments---------------
print(20*"-","Varying Arguments[xargs]",20*"-")

def multiply(*numbers):
    print(numbers,type(numbers))
    total=1;
    for number in numbers:
        total=total*number
    return  total;

result=multiply(5)
print(result)

result=multiply(5,6,7)
print(result)

result=multiply(1,2,3,4,5)
print(result)
# ------------------------------------------------------------
def calculate_cart_value(*cart_items):
    print(cart_items,type(cart_items))
    total=0;
    for cart_item in cart_items:
        item_cost=cart_item["qty"]*cart_item["price"]
        total=total+item_cost

    return total


# ------------------------------------------------
result=calculate_cart_value(
    {"item":"P1","qty":1,"price":10},
    {"item":"P2","qty":1,"price":20},
    {"item":"P5","qty":1,"price":50})
print(result)

result=calculate_cart_value(
    {"item":"P1","qty":2,"price":10},
    {"item":"P2","qty":5,"price":20},
);
print(result)

















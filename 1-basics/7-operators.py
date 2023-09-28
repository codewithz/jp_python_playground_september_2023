# and
# or
# not

# Loan Processing System

high_income=False
good_credit=True
is_student=True

print(40*"-")

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# --------------------------------------

print(40*"-")

if(high_income or good_credit) and is_student:
    print("Eligible")
else:
    print("Not Eligible.")

# ------------- Ternary Operator-------------

print(40*"-")

age=19
#
# message=""
#
# if age>18:
#     message="Eligible Age"
# else:
#     message="Not Eligible Age"

message= "Eligible Age" if age>18 else "Not Eligible Age"

print("Message:",message)

# ---------- Chaining Comparison Operator -------------

print(40*"-")

#  age should be between 18 and 65

if age>18 and age<65:
    print("Eligible")

if 18 <= age <=65:
    print("Elgible from comparision operator")
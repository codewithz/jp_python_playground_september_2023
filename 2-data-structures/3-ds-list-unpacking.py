numbers=[1,2,3,4,4,4,4,4,4,4,5,6]

# first,second,third,fourth,second_last,last=numbers
first,second,third,*others,second_last,last=numbers

f,s,t,*o,sl,l=numbers


# first=numbers[0];
# second=numbers[1];
# third=numbers[2];
# fourth=numbers[3];
# second_last=numbers[4];
# last=numbers[5];

print("First",first)
print("Second",second)
print("Third",third)
print("Others",others)
print("Second Last",second_last)
print("Last",last)
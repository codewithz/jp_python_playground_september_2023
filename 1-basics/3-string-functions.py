name='Zartab'
print(name)
print(type(name))
print(dir(name))

# Strings in python can be enclosed in "some string " or 'some string'
#  If you intend to use '' as a part of string , then use the string in ""

sentence ="i don't know where they are"
print(sentence)

sentence ='i know where they are'
print(sentence)

# Multi Line String

paragraph="""
India is my country.
All Indians are my brothers and sisters
I Love my country
And I am proud of it
          """

print(paragraph)

#String in python comes with indexes
#Stirng in python are like arrays

word="Kitkat"
print(word)
print(word[1])
print(word[2])
print("Word[1:3]",word[1:3])
print("Word[-3]",word[-3])
#
# print("Word[8]",word[8])
# IndexError: string index out of range

print("Word[0:20]",word[0:20])
 #Starts with 1 of zero index and gives till end
print("Word[1:]",word[1:])

#Starts from 0 of zero based index and give till 5 of one based
print("Word [:5]",word[:5])

# Clone
print("word[:]",word[:])

# Length

print("Length",len(word))

#Trimming -- strip()

word_with_spaces="   Hello World   ";
print(word_with_spaces)
print("Length before strip",len(word_with_spaces))
word_with_spaces=word_with_spaces.strip()
print(word_with_spaces)
print("Length after strip",len(word_with_spaces))

print()
print()

# Casings

company="jp morgan"
print("Company:",company)
company=company.upper()
print("Company:",company)

sentence="I AM HAPPY TO BE HERE"
print("Sen:",sentence)

sentence=sentence.lower()
print("Sen:",sentence)

sentence=sentence.capitalize()
print("Sen with Capitalize:",sentence)

sentence=sentence.title()
print("Sen with Title:",sentence)

# name=input("Enter your name:")
# print(name.upper())

#Split a String

line1="1,Tom,IT,Developer,30000"
line2="Hello How are you"

print("O1:",line1)
print("O2:",line2)

data1=line1.split(",")
print(data1)
print(type(data1))

data2=line2.split(" ")
print(data2)
print(type(data2))

#Format Functions

line ="My name is Zartab , I am {} years old"
age=33

fline=line.format(age)
print("O:",line)
print("F:",fline)

line ="My name is {} , I am {} years old"
name="Micheal"
age=35

fline=line.format(name,age)
print("O:",line)
print("F:",fline)

print()
# Numbered Formatting

line="Hey I am a {0}, I train my {1},{0} trains a {1}"
fline=line.format("Trainer","Trainee")
print("O:",line)
print("F:",fline)

print()
# Named Formatting

line="Hey I am a {trainer}, I train my {trainee},{trainer} trains a {trainee}"
fline=line.format(trainer="Trainer",trainee="Trainee")
print("O:",line)
print("F:",fline)

print()
# Count
name='Zartab'
a_count=name.count('a')
print("Count of a in",name,'is',a_count)

# Starts and Ends with

print("Starts with z",name.startswith("z"))
print("Starts with Z",name.startswith("Z"))
print("Starts with a",name.startswith("a"))
print("Starts with Zar",name.startswith("Zar"))
print("Ends with b",name.endswith("b"))
print("Ends with B",name.endswith("B"))
print("Ends with x",name.endswith("x"))
print("Ends with tab",name.endswith("tab"))

print()
# Escape Characters

# \n -- new line
# \t -- tab
# \\ -- backslash
# \" -- double quote

text="This is a backslash \\"
print(text)
text="These are two backslashes \\\\"
print(text)
text="I work for \"JP Morgan\""
print(text)


line ="JP Morgan have offices in Mumbai,Bengaluru,Hyderabad"
line=line.lower()
mumbai_in_line="mumbai" in line
print("Is Mumbai used in the line",mumbai_in_line)

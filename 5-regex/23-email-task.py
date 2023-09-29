import re

word_list = ['zartab@codewithz.com',
             'zartab.n@uni.edu',
             'zartab-n-1312@my-company.net',
             'zartab#n#1312@my-company.net']


pattern='^[a-zA-Z][A-Za-z0-9_.]*@[a-zA-Z][A-Za-z0-9-.]*\.(com|edu|org|net)'

pattern="^[a-zA-Z][A-Za-z0-9_.-]*@[a-zA-Z][a-zA-Z0-9-.]*\.(com|edu|net|org)"


for word in word_list:
    result=re.match(pattern,str(word))
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")
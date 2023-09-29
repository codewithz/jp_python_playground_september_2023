import re

word_list = ['zartab@codewithz.com',
             'zartab.n@uni.edu',
             'zartab-n-1312@my-company.net']


pattern=''


for word in word_list:
    result=re.match(pattern,str(word))
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")
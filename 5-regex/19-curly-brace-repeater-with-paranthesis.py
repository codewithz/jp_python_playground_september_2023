import re

word_list = ['haaaa','ha', 'hahahahaha', 'hahaha', 'hahahaha', 'haha',
             'hahahahahaha', 'hahahahahahahaha', 'hahahahahahahahaha']

pattern='(ha){4,9}'


for word in word_list:
    result=re.match(pattern,str(word))
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")
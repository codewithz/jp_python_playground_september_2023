import re

word_list = ['joo', 'aoo','boo','coo', 'Koo', 'Loo', 'poo', 'moo', 'zoo', 'hoo']

pattern='[a-cj-mJ-Mz]oo'

for word in word_list:
    result=re.match(pattern,word)
    if result:
        print(f"{word} MATCHES FOR {pattern}")
    else:
        print(f"{word} doesn't matches for {pattern}")


import re
text = "Steve Smith is a Rockstar. Yup!! he is a RockSStar"
pattern = r"Rock[A-Z]+tar"

# match function 
match = re.search(pattern,text)
if match:
    print("We got it")   
else:
    print("Its not there mate")


# finditer function will take care of every pattern it finds and gives the span for every find. It can be used as alternative of search function as it only finds the first match 
matches = re.finditer(pattern,text)
for match in matches:
    print(match)


# findall function 
match = re.findall("is",text)
print(match)

# split function
match = re.split("\s",text,3)
print(match)

# sub function 
match = re.sub("\s","-space-",text,2)
print(match)


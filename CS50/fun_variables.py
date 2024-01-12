# name = input("What is your name, babe\n")


# print("hello, " + name) 
# print("Myself",name,sep="???")
# sep means what will happen in the seperator actually

# print("hello, ",end="") #Overriding the value of end
# print(name) 

# print("hello,\"friend\" ") #this is how we input double quotes

# print(f"hello, {name}")

# String methods

# name = name.strip() #remove the whitespace from str

# Capitalize user'name but this will only capitalize the first letter 
# name = name.capitalize()

# this will capitalize every first letter of every word 
# name = name.title()


# name = name.strip().title(); #also can do 

# name = input("Type ur name : ").strip().title() # can do this as well



name = input("Type : ").strip().title()

# split user name into first and last name

first,last = name.split(" ")
print(f"hello, {first}") 


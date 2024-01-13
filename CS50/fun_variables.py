# name = input("What is your name, babe\n")
"""
this is a multi line comment

"""



# what's inside print function ?

# print(*obj,sep=' ',end='\n',file=sys.stdout, flush = False) # the actual print statement with the parameters in official docs
# u can past any no of strings, seperator in b/w the arguments is a gap, and print statement is bydefault end via a newLine

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



# name = input("Type : ").strip().title()

# split user name into first and last name

# firstName,lastName = name.split(" ")
# print(f"Hello, {firstName}")


# integers 

# x = int(input("x = "))
# y = int(input("y = "))
# print(x+y)

#floats

# x = float(input("x = "))
# y = float(input("y = "))

# z = round(x+y,3) # round(number[, ndigits])
# z = round(x+y)

# print(f"{z:,}")  # put a comma after every 3 digits - US based

# z = round(x/y,2)

# z = x/y
# print(f"{z:.2f}") # f string approach to solve the very same problem as we did before 




# functions
# def hello(to):       #define
#     print("hello,",to)



# if i want to give a default value to my "to " variable
# def hello(to="world"):       #define
#     print("hello,",to)

# hello()
# name = input("What's ur name? ")
# hello(name)
# print(name)


# there seems to be a problem like suppose if you are having ur function down below where ur calling it you will eventually get an error cause it is not defined at that moment whre ur calling it so basically python does not even know that the function even exists
# although there can be one solution to this one : 

# def main():
#     hello()
#     name = input("What's ur name? ")
#     hello(name)

# def hello(to="world"):       #define
#     print("hello,",to)
    
# main()


# def main():
#     x = int(input("x = "))
#     print("x squared is ",square(x))
    
# def square(n):
#     # return n**2
#     return pow(n,2)

# main()

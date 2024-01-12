# class Person:
    

#     def __init__(self,name,work):
#             # print("Ye constructor bhaishab bin bulae mehmaan hai jo har jagah muh uthake aa jate hai ")
#             self.name = name
#             self.work = work
    
#     def printDetails(self):
#         print(f"{self.name} & {self.work}")

# a = Person("Mera naam naam hai","mai kaam karta hu")
# # a.name = "Steve Smith"
# a.printDetails()

# b = Person("Mera naam kaam hai ","mai naam karta hu")
# b.printDetails()



# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f"Name : {self.name} ID : {self.id}")
        
# class Programmer(Employee):
#     def __init__(self, name, id,experience):
#         super().__init__(name, id)
#         self.experience = experience
#     def showLan(self):
#         print(f"Experience : {self.experience} years") 








# e1 = Employee("Parth",420)
# e1.showDetails()

# e2 = Programmer("Steve",49,2)
# e2.showDetails()
# e2.showLan()


# class Employee:
#     def __init__(self):
#         self.__name = "Steve"
    
# a = Employee()
# # print(a.name) # cannot be accessed directly

# print(a._Employee__name)  # can be accessed directly

# print(a.__dir__())                      


# class Math:
#     def __init__(self,num):
#         self.num = num
            
#     def addToNum(self,n):
#         self.num+=n
    
#     @staticmethod
#     def add(a,b):
#         return a+b
    
# # a = Math(5)
# # print(a.num)
# # a.addToNum(6)
# # print(a.num)

# a = Math(2)

# b = Math(1)

# print(Math.population)


# print(Math.add(49,59))

# class Employee:
#     def __init__(self,name):
#         self.name = name
#     def showDetails(self):
#         print(f"Name : {self.name} ")
        
# emp1 = Employee("Steve")

# emp1.showDetails()
# Employee.showDetails(emp1)



import re

# raw = r"Hello\nWorld"
# normalString = "Hello\nWorld"

# print(raw,normalString)

text = "Steve Smith is a RRockstar. Ahh ya mate he is a Rockstar"
pattern = r"[A-Z]+ockstar"
# match = re.search(pattern,text)
# if match:
#     print("We got it")   
# else:
#     print("Its not there mate")

# matches = re.finditer(pattern,text)
# for match in matches:
#     print(match)

# match = re.findall("is",text)
# print(match)

# match = re.split("\s",text,3)
# print(match)

match = re.sub("\s","-space-",text,2)
print(match)


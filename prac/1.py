
class Human:
    population=0
    def __init__(self,name,age,married):
        self.name = name
        self.age = age
        self.married = married
        Human.population+=1
    def printDetails(self):
        print(f"{self.name} who ages {self.age} \n Married status : {self.married}")

human1 = Human("Parth",18,False)
human2 = Human("Steve",35,True)
human1.printDetails()
human2.printDetails()
print(Human.population)
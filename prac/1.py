
class Human:
    population=0
    def __init__(self,gender,age):
        self.gender = gender
        self.age = age
        Human.population+=1
    @staticmethod
    def speak():
        print("Human is speaking")
    
    def studySubject(self,subject):
        print(f"Human studies {subject}")

class Human1(Human):
    def __init__(self,name, gender, age):
        super().__init__(gender, age)
        self.name = name

    def setPersonalDetails(self,married,subject,athlete):
        self.married = married
        self.subject = subject
        self.athlete = athlete
    def getSubject(self):
        print(f"{self.name} studies {self.subject}")
    def getMarriedStatus(self):
        return self.married
    

    def getAllDetails(self):
        print(f"Name : {self.name}\nGender : {self.gender}\nAge : {self.age}\n",end="")
        if(self.getMarriedStatus()):
            print("Married Status : Married")
        else:
            print("Married Status : Unmarried")

obj1 = Human1("Steve","Male",19)
obj1.setPersonalDetails(False,"JavaScript",True)
obj1.getSubject()
obj1.getAllDetails()




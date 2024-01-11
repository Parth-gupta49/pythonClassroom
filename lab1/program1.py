# Class 
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    # This method will be overridden by subclasses
    def make_sound(self):
        pass  


# Inheritance
class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks: {self.sound}"


class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: {self.sound}"


# Polymorphism
def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())


# Encapsulation and Data Abstraction
class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder  # Encapsulation 
        self._balance = balance  # Encapsulation 


    def deposit(self, amount):
        self._balance += amount


    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")


    def get_balance(self):
        return self._balance


# Objects
if __name__ == "__main__":
    # Objects of Animal class
    dog = Dog("Buddy", "Woof")
    cat = Cat("Whiskers", "Meow")


    # Polymorphism
    animals = [dog, cat]
    animal_sounds(animals)


    # Objects of BankAccount class
    account1 = BankAccount("Tejas", 1000)
    account2 = BankAccount("Sree", 500)
    
    # Encapsulation and Data Abstraction
    print(f"\n{account1._account_holder}'s Balance: ${account1.get_balance()}")
    print(f"{account2._account_holder}'s Balance: ${account2.get_balance()}")


    account1.deposit(500)
    print("\nAmount deposited in Tejas account: 500")
    account2.withdraw(200)
    print("Amount withdrawn from Sree account: 200")
    
    print(f"\n{account1._account_holder}'s Updated Balance: ${account1.get_balance()}")
    print(f"{account2._account_holder}'s Updated Balance: ${account2.get_balance()}")
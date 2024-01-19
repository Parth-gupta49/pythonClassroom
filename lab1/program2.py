# # Syntax Error
'''print "Hello World" '''


def main():

    print("press 1 for Type error")
    print("press 2 for index error")
    print("press 3 for name error")
    print("press 4 for keyValueError error")
    print("press 5 for Attribute error")

    choice = int(input("Give Input: "))
    match choice:
        case 1:
            typeError()
        case 2:
            indexError()
        case 3:
            nameError()
        case 4:
            keyValueError()
        case 5:
            attributeError()






# # Type Error
def typeError():
    try:
        
        result = "str" + 5
    except TypeError as e:
        print(f"TypeError: {e}")


# # Index Error
def indexError():
    try:
        numbers = [1, 2, 3]
        print(numbers[5])
    except IndexError as e:
        print(f"IndexError: {e}")

def nameError():
# # Name Error
    try:
        print(whereisVariable)
    except NameError as e:
        print(f"NameError: {e}")


# # Key/Value Error
def keyValueError():
    try:
        my_dict = {"name": "John", "age": 25}
        print(my_dict["gender"])
    except KeyError as e:
        print(f"KeyError: {e}")


def attributeError():
# # Attribute Error
    try:
        class MyClass:
            pass
        obj = MyClass()
        print(obj.attributeCallingOverHereMate)
    except AttributeError as e:
        print(f"AttributeError: {e}")


# # IO Error
# try:
    
#     with open("nonexistent_file.txt", "r") as file:
#         content = file.read()
# except IOError as e:
#     print(f"IOError: {e}")


# try:
   
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print(f"ZeroDivisionError: {e}")


# # ImportError
# try:
    
#     import non_existent_module
# except ImportError as e:
#     print(f"ImportError: {e}")


main()
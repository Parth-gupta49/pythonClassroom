# Syntax Error
'''print "Hello World" '''


# Type Error
try:
    
    result = "str" + 5
except TypeError as e:
    print(f"TypeError: {e}")


# Index Error
try:
    
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError as e:
    print(f"IndexError: {e}")


# Name Error
try:
    
    print(undefined_variable)
except NameError as e:
    print(f"NameError: {e}")


# Key/Value Error
try:
   
    my_dict = {"name": "John", "age": 25}
    print(my_dict["gender"])
except KeyError as e:
    print(f"KeyError: {e}")


# Attribute Error
try:
    
    class MyClass:
        pass


    obj = MyClass()
    print(obj.attribute)
except AttributeError as e:
    print(f"AttributeError: {e}")


# IO Error
try:
    
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except IOError as e:
    print(f"IOError: {e}")


try:
   
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")


# ImportError
try:
    
    import non_existent_module
except ImportError as e:
    print(f"ImportError: {e}")

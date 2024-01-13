name = input("Name? ")

# if   name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who is that")
    
# keyword : match ( "switch case" in case of other languages)
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:                   # default in case of python
        print("Who?")
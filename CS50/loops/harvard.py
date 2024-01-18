# students = ["Parth","Steve","David"] # list

# for student in students:
#     print(student)

# for i in range(len(students)):  # length function 
#     print(i + 1, students[i])


# Dictionary
# students = {
#     "Parth":"bangalore",
#     "Steve":"Sydney",
#     "David J Malan":"Washington"
    
    
#     }

# print(students["Parth"])

# when we iterate through dictionary in python it is actually initializing i with the key(student's name in this case) every single time
# so when the following loop starts the value it is holding at the start is Parth, then Steve and so on ..
# and as we were able to iterate through the list using indices namely 0,1,2... 
# we can do the same for the dictionary as well but here the indices 0,1,.. wont work
# instead we can actually give the key values so to get the value of that key..and thats how we iterate through the dictionary in python

# for student in students:
#     print(student,students[student], sep=",\t")




# students = [
#     {"name":"Parth","house":"Bangalore","hobby":"coding"},
#     {"name":"Steve","house":"Sydney","hobby":"Cricket"},
#     {"name":"David","house":"Washington","hobby":"Teaching"},
#     {"name":"Prick","house":"Melbourne","hobby":None}
# ]

# for student in students:
#     print(student["name"],student["house"],student["hobby"],sep=", ")



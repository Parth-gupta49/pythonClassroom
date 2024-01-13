score = int(input("Score: "))

# if score>=90 and score<=100:
#     print("A")
# elif score>=80 and score < 90:
#     print("B")
# elif score>=70 and score < 80:
#     print("C")
# elif score>=60 and score < 70:
#     print("D")
# else:
#     print("F")
    
# better code ?
# if 90<=score<=100:
#     print("A")
# elif 80<=score<90:
#     print("B")
# elif 70<=score<80:
#     print("C")
# elif 60<=score<70:
#     print("D")
# else:
#     print("F")  
    
# further better code?
# Ah yeah it is.. suppose if we know that the input which we are getting is in between 0 and 100 so we can just improve our logic written above like this : 
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F") 
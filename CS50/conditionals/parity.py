def main():
    x = int(input("x = "))
    if(is_even(x)):
        print("Even")
    else:
        print("Odd")

# def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

# cool way to write the above function : 
def is_even(n):
    # return True if n % 2 == 0 else False
    # even better code 
    return ( n % 2 == 0 )
    
main()
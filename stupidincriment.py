# x = ("Enter a number pls:")
# try :
#     x = int(input(x))
#     print(x - 1)
# except :
#     print("That is not a number")

def decimal():
    x = input("Enter a number please: ")
    try:
        x = float(x)  
        if x < 0:
            x = int(x)
            print(x - 1)
        else:
            x = float(x)
            print(x + 1)
    except ValueError:
        print("That is not a valid number")

decimal()

    
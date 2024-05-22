for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 7 == 0:
        print("FizzBazz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 7 == 0:
        print("Bazz")
    else:
        print(i)
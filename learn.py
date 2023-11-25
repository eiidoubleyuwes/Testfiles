#indefinite loop
# while True :
#     x = input(">")
#     if x == "stop" :
#         print("Correct")
#         break
#     print("not key word")

#definite loop
# x = 5
# for i in range(x):
#     print(i-1)

#check smallest number in array
smol = 100
for big in [1,23,400,0,0.00,34,100,34]:
    if big < smol:
        smol = big
        print(big,smol)
    
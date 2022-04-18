# lst = [1,2,3,4,5]
# print(type(lst))
# nums = list(range(1,101))
# print(nums)
# lst = list("Ashish")
# print(lst)
# for x in lst:
#     print("The value of x: ",x)

# for i in range(1,5):
#     print("The value of i: ",i)

# lst = list("python")
# for i in lst:
#     if(i == "h"):
#         print("h found")
#     print(i)
# print("endline")
# lst = list("python")
# for i in lst:
#     if(i == "h"):
#         print("h found")
#         break
#     print(i)
# print("endline")
# lst = list("python")
# for i in lst:
#     if(i == "h"):
#         print("h found")
#         continue
#     print(i)
# print("endline")

# Console based simple calculator
print("Welcome to simple calculator")
while(True):
    fstnum = float(input("Enter the first number"))

    secnum = float(input("enter the second number"))

    cos = int(input(
        "Choose your option \n1.Sum \n2.subtractio \n3.Multiplication \n4.Division \n5.Exit "))
    temp = 0

    if(cos == 1):
        temp = fstnum+secnum
        print("Your sum is ", temp)

    elif(cos == 2):
        temp = fstnum-secnum
        print("Your sub is ", temp)

    elif(cos == 3):
        temp = fstnum*secnum
        print("Your sub is ", temp)

    elif(cos == 4):
        if(secnum == 0):
            print("cannot be divisible by 0")
        else:
            temp = fstnum/secnum
            print("Your sub is ", temp)

    elif(cos == 5):
        break

    else:
        print("you have choosed wrong option")

print("You have exit")

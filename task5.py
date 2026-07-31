#greatest of three num
num1 = int(input("enter  first num:"))
num2 = int(input("enter second num:"))
num3 = int(input("enter  third num:"))
if (num1 >= num2 and num1 >= num3):
    print(num1, "is the greatest num")
elif (num2 >= num1 and num2 >= num3):
    print(num2, "is the greatest num")
else:
    print(num3, "is the greatest num")

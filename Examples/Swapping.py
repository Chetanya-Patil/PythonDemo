# Swapping 2 numbers

num = input("Enter the number one") # This is to take input from outside

num1 = 10
num2 = 20

#Approach 1
print("Value before swapping:",num1,num2)
num1,num2 = num2,num1
print("Value after swapping of :",num1,num2)

#Approach 2
# temp1 = num1
# num1 = num2
# num2 = temp1
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan 
# Section: 574
# Assignment: 6-3
# Date: 1 10 22
#



num = int(input("Enter an integer: \n"))# we get the first integer
num2 = int(input("Enter another integer: \n"))# get the second integer

for i in range (1,101):#sets up a for loop as we know we want 100 instances
    if i % num == 0 and i % num2 == 0:#prints Howdy Whoop if evenly divisble by both
        print("Howdy Whoop")
    elif i % num == 0:
        print("Howdy")#prints howdy if evenly divisible by num
    elif i % num2 == 0:
        print("Whoop")#prints whoop if evenly divisible by num2
    else:
        print(i)#rints i if non of the other previous test cases passed
    

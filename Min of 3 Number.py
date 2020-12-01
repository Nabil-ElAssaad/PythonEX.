First  = input("Enter the first value\n")
Second = input("Enter the 2nd value\n")
Third  = input("Enter the Third value\n")
Max = First if First > Second and First > Third  else Second if Second > Third else Third
print(" The Max number is ", Max)
print("-----------------------------------------------------------------------------")
First  = input("Enter the first value\n")
Second = input("Enter the 2nd value\n")
print("Both have same number" if First==Second else " First Number is bigger than Second Number " if First>Second
      else " Second Number is bigger than First Number")
print("-----------------------------------------------------------------------------")
import math
Q = int (input("Enter radius\n"))
AreaOfCircle = math.pi * (Q ** 2)
print(AreaOfCircle)
x= int(input("Enter the num: "))
def factorial(x):
    
    if x < 2:
        return 1
    else:
        return x * factorial(x-1)
result = factorial(x)
print ("Factorial of 5 is: ",result)
#######################################################################################
import math
x= int(input("Enter the num: "))

squareroot = math.sqrt(x)
logarithm = math.log(x)
sine = math.sin(x)

print("square root : ",squareroot)
print("laogarithme: ",logarithm)
print("sine: ",sine)

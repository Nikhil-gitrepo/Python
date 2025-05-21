
#reuse the code.

# A= "Hello "
# B= "world"
# def str1():
#     print (A + B)
# str1()

#retrun the value

# def add(a, b):
#     c= a+b
#     return c
# result=add(5, 10)
# print(result)

#passing functiom as argument
# def add(x,y):
#     return(x + y)
# def square(z):
#     return(z * z)
# result= square(add(4,3))
# print(result)
    
#factorial 
def factirial(n):
    if n < 2:
        return 1
    else:
        return n * (factirial(n-1))

result = factirial(5)
print (result)
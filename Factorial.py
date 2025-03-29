def factorial(x):
    '''this is a recursive fuction to find the factorial of an integers'''
    
    if x==0 or x==1:
       return 1
    else:
        #calling fuction inside a function
        return x*factorial(x-1)
    
    #display result
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 4:",factorial(4))
print("the factorial of 5:",factorial(5))
print("the factorial of 10:",factorial(10))
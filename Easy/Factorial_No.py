# Factorial Number 5!=5*4*3*2*1=120

def factorial(n):
    assert n>0 and int(n)==n
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))

# 2nd Approach 

factorial = 1

num= int(input("Enter the number "))

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("The factorial of ",num, "is", factorial)
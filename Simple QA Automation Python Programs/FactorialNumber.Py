"Find the the factorial of number : 5!=1*2*3*4*5=120 "

#Approach-1

def factorial(n):
    assert int(n)>=0, "The integer should be positive "
    
    if n in [0,1]:
        return n
    else:
        return n*factorial(n-1)

print(factorial(5))    


#Approach-2

factorial=1
n=6

if n<0:
    print(' Factorial does not exits for negative number')
elif n==0:
    print('Factorial of number 0 is 1 ') 
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)
    
    






        
    


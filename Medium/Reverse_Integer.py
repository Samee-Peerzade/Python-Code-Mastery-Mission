""" 
7. Reverse Integer
Medium
11.7K
12.8K
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

"""

# 123%10=3, 123/10=12, 12%10=2, 3*10=30+2=32
import math

def reverse(x):
    #Integer.MAX_VALUE = 2147483647 (END WITH 7)
    #Integer.MAX_VALUE = -2147483648 (END WITH -8)
    
    min=-2147483648 #-2^31
    max=2147483647 #2^31
    
    res=0
    
    while x:
        digit=int(math.fmod(x,10)) #-1%10=9
        x=int(x/10)                 #-1//10=-1
        
        if (res>max//10 or 
            (res==max//10 and digit >= max% 10)):
            return 0
        
        if (res<min//10 or 
            (res==min//10 and digit <= min% 10)):
            return 0
        
        res=(res*10)+digit
        
    return res


print(reverse(-123))
        

        
# Approach -2
"""
# Conditions are 1) Reverse the integer 2) If num smaller than 0: sign should be Negative 

Reverse Integer Algorithm : eg: 123  
1) rem = num % 10           # remove last digit 3, remainder=3 - Extraction of last digit
2) sum = sum *10 + rem      # shift 3 to first position => sum=0*10+3=3
3) num = num // 10          # 12 / 10 = 2 as remainder 
                            3*10+2=32 and last step : 1/10 and 32*10=320+1=321
     
input=-123 then condition if(num<0) add negative sign. 

"""

        
        
def reverse_signed(num):
    sum=0
    sign=1
    
    if num<0:
        sign=-1
        num=num*-1
        
    while num>0:
        rem=num%10
        sum=sum*10+rem
        num=num//10
        
    if not -2147483648<sum<2147483647:
        return 0
    return sign*sum

print(reverse_signed(123))
        
    
        
        
        
        
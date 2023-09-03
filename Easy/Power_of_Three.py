""" 
326. Power of Three
Easy
2.8K
257
Companies
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

"""


def isPowerofThree(n):
    if n<=0:
        return False
    
    while n%3==0:
        n/=3
        
    return n==1

print(isPowerofThree(27))  # Output: True
print(isPowerofThree(0))   # Output: False
print(isPowerofThree(-1))  # Output: False


# 2nd Approach - Recursive Method:

def isPowerOfThree(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return isPowerOfThree(n // 3)

print(isPowerOfThree(27))  # Output: True
print(isPowerOfThree(0))   # Output: False
print(isPowerOfThree(-1))  # Output: False






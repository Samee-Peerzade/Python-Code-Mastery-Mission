"""50. Pow(x, n)
Medium
8.6K
8.5K
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000

Explanation: 2-2 = 1/22 = 1/4 = 0.25

# 
Step 1: Recursive case - the flow x^a + x^b = x^a+b = x^n= x*x^n-1
    
step2: Base Case - the stopping criterion n=0
    
step 3: Unintentional case- the constraint
1) power(-1,2) ??
2) power(3.2,2)??
3) power(2,1.2) ??
4) power(2,-1)

"""


def power(base,exp):
    
    assert int(exp)==exp, 'The exponent must be integer number only'
    
    if exp==0:
        return 1
    
    elif exp<0:
        return 1/base*power(base,exp+1)
    
    return base*power(base, exp-1)    #Formula

print(power(4,3)) 









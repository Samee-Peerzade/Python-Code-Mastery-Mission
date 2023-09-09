""" 
Find the maximum product of 2 integers in an array where all elements are positive 

array=[1,7,3,4,5,9]   # max elements are 9 and 7 => product of 9*7 = 63

"""

def max_product(array):
    max1,max2=0,0
    
    for i in array:
        if i>max1:
            max2=max1
            max1=i
            
        elif i>max2:
            max2=i
            
            
    return max1*max2

array=[1,7,3,4,5,9]
print(max_product(array))            
            
            
            
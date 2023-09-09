"""  
input=[25,3,2,1,4]
1st largest: 25
2nd largest : 4 
output=[25,4]

"""

def max_elements(array):
    max1,max2=0,0
    
    for i in array:
        
        if i>max1:
            max2=max1
            max1=i
        
        elif i>max2:
            max2=i
            
    return max1,max2

print(max_elements([25,3,2,1,4]))


#easy
# 2) Find the maximum element in array 
#input=[25,3,4,3,50,100]   # output=100

def find_max_element(array):
    
    max=array[0]
    
    for i in array:
        if i>max:
            max=i
    return max

print(find_max_element([25,3,4,3,50,100]))  






            
    
    
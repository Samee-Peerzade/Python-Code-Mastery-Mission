""" 
"""


def twoSum(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
            
            
target=9
nums=[2,7,3,4]
print(twoSum(nums))

# 2nd Aprroach

def two_sum(nums,target):
    seen={}
    
    for i,num in enumerate(nums):
        complement=target-num
        
        if complement in seen:
            return [seen[complement],i]
        
        seen[num]=i
        
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")
            
            
            
            
            
            
""" 
283. Move Zeroes
Easy
15.1K
380
Companies
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


"""

def movezeroes(nums):
    l=0
    for i in range(len(nums)):
        if nums[i]:
            nums[l],nums[i]=nums[i],nums[l]
            l+=1
            
    return nums
            
nums=[0,1,0,3,12]

print(movezeroes(nums))


# 2nd Approach:

def moveZeroes(nums):
    index = 0

    for num in range(len(nums)):  # Change "for num in len(nums)" to "for num in range(len(nums))"
        if nums[num] != 0:
            nums[index] = nums[num]
            index += 1

    while index < len(nums):
        nums[index] = 0
        index += 1

nums = [0, 2, 3, 0, 12]
moveZeroes(nums)
print(nums)




        
        
        
        
        
        
        
            
        
    
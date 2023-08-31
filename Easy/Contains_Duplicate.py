""" 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    def containsDuplicate(self, nums):
        seen = set()
    
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        
        return False

solution_instance = Solution()
print(solution_instance.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))








"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
"""

def longestCommonPrefix(strs):
    if len(strs)==0:        # If length of string is 0 then return None
        return("")
    if len(strs)==1:       # if there is single element return that
        return(strs[0])
    
    prefix=strs[0] # flower
    
    
    plen=len(prefix) # 6 
       
    for i in strs[1:]:    # i=flow index 2
        
        while prefix != i[0:plen]:
            prefix=prefix[0:(plen-1)]
            plen -=1
            
            if plen==0:
                return("")
    return(prefix)

strs=["flower","flow","flight"]
print(longestCommonPrefix(strs))

    
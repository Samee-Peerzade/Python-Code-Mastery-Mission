""" 
387. First Unique Character in a String
Easy
8.2K
260
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""


#hashmap - approach-1
def firstuniquechar(s):
    import collections
    
    counter=collections.Counter(list(s))
    
    for i in range(len(s)):
        if counter.get(s[i])==1:
            return i
    return -1

print(firstuniquechar("loveleetcode"))


#Approach-2

def firstunique(s):
    st_map={}
    for i in range(0,len(s)):
        if s[i] not in st_map:
            st_map[s[i]]=True
           
            
        else:
            st_map[s[i]]=False
            
            
    for i in range(0,len(s)):
        if st_map[s[i]]:
            return i
    return -1
            
print(firstunique("loveleetcode"))
            








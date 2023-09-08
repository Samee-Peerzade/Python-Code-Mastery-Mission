""" 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""
#Approach-1
def validAnagram(s,t):
    sorted_s=sorted(s)
    sorted_t=sorted(t)
    return sorted_s==sorted_t


print(validAnagram("anagram","nagaram"))

#Approach-2: HashMap


def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    
    count_s,count_t={},{}
    
    for i in range(len(s)):
        count_s[s[i]]=1+count_s.get(s[i],0)
        count_t[t[i]]=1+count_t.get(t[i],0)
        
        
    return count_s==count_t

print(isAnagram("rat","car"))

    
    
    
    



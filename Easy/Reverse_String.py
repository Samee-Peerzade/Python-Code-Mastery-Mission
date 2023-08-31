""" 
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""
#Approach - 1

def reverse_string(string):
    return string[::-1]

print(reverse_string(["h","e","l","l","o"]))

#Approach-2 - Two Pointer

def reverse(string):
    l = 0
    r = len(string) - 1
    
    while l < r:
        string[l], string[r] = string[r], string[l]
        l = l + 1
        r = r - 1
# Example usage
char_list = ["s", "a", "m"]
reverse(char_list)
print(char_list)




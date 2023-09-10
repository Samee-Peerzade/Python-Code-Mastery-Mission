# O(n) 
""" 
20. Valid Parentheses
Easy
21.9K
1.4K
Companies
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""

def valid_parentheses(s):
    stack=[]
    closeToOpen={ ")":"(",    "]":"[",  "}":"{"  }  #hashMap => mapping the parentheses
    
    for c in s:                 
        if c in closeToOpen:                            # if character in closeToopen
            if stack and stack[-1]==closeToOpen[c]:     # checkif stack is not empty and last character is top of stack
                stack.pop()                             #If match succesful then pop it of
            else:
                return False
        else:
            stack.append(c)
            
    return True if not stack else False

print(valid_parentheses("(("))










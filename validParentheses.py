'''
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


'''

#########################################
'''

we cannot start with the any closing parenthesis
 - that means we cannot add a closing parenthesis to (the beginning of the stack)


stack data structure problem

O(n) - we go through each of the bracket - once
O(n) - memory -  the stack could be up to the size of the input


//
any opening parenthesis you see - place on stack
 - you can use hash map - for the pair


'''

############################################



'''

    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif i==')' and len(stack) !=0 and stack[-1] == '(':
                stack.pop()
            elif i==']' and len(stack) !=0 and stack[-1] == '[':
                stack.pop()
            elif i=='}' and len(stack) !=0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return len(stack) == 0

'''

class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for i in s:
            if i in pairs:
                # if its is a closing parn - then look up the pair in the hashMap - and pop it - if it is not empty
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        return True if not stack else False



'''
simple concepts:

s = []

if s: print("..") -> a way of checking if s is empty or not
if s ==> would mean, if something is in 's'
'''































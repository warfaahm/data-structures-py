# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine
# if the input string is valid.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for a in s:
            if a in ['[', '(', '{']:
                stack.append(a)
            else:
                if not stack:
                    return False
                if a == ')' and stack[-1] != '(':
                    return False
                if a == '}' and stack[-1] != '{':
                    return False
                if a == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        return not stack

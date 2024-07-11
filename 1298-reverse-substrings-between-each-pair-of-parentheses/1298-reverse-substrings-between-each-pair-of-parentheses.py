class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ')':
                in_bracket = []
                while stack and stack[-1] != '(':
                    in_bracket.append(stack.pop())
                stack.pop()
                for c in in_bracket:
                    stack.append(c)
            else:
                stack.append(char)
        
        return ''.join(stack)
        
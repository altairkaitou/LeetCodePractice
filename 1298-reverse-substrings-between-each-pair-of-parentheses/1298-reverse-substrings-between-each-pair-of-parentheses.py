class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack_bracket = []

        for char in s:
            if char == ')':
                in_bracket = []
                while stack_bracket and stack_bracket[-1] != '(':
                    in_bracket.append(stack_bracket.pop())
                stack_bracket.pop()
                for c in in_bracket:
                    stack_bracket.append(c)
            else:
                stack_bracket.append(char)
        
        return "".join(stack_bracket)
        
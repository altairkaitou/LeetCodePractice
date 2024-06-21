class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        n = len(s)

        for i in range (n):
            if i % 2 == 0:
                result += s[i]
            else:
                digit = int(s[i])

                result += chr(ord(s[i - 1]) + digit)

        return result 
        
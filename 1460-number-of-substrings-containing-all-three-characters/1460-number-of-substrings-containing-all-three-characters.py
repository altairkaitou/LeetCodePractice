class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c = 0, 0, 0
        result = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] == 'a':
                a += 1
            elif s[right] == 'b':
                b += 1
            elif s[right] == 'c':
                c += 1
            
            while a > 0 and b > 0 and c > 0:
                result += len(s) - right

                if s[left] == 'a':
                    a -= 1
                elif s[left] == 'b':
                    b -= 1
                elif s[left] == 'c':
                    c -= 1
                left += 1
            right += 1
        return result




        
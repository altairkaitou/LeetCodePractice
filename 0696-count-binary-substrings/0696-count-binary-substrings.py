class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        prev = 0 
        current = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                result += min(prev, current)
                prev = current
                current = 1
            else:
                current += 1
        
        result += min(prev,current)
        return result
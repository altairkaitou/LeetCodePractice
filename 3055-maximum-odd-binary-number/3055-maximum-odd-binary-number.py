class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [c for c in s]
        left = 0

        for i in range(len(s)):
            if s[i] == '1':
                s[i], s[left] = s[left], s[i]
                left += 1
        s[left - 1], s[len(s) - 1] = s[len(s) - 1], s[left -1 ]
        return "".join(s)
        

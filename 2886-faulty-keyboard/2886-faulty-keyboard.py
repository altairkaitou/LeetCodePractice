class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for char in s:
            if char == 'i':
                result.reverse()
            else:
                result.append(char)
        
        return "".join(result)


        
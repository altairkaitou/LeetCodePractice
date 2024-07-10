class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []
        def recurs(string1):
            if len(string1) == n:
                result.append(string1)
                return
            
            if len(string1) == 0 or string1[-1] == '1':
                recurs(string1 + '0')
            
            recurs(string1 + '1')

        recurs("")

        return result
        

        
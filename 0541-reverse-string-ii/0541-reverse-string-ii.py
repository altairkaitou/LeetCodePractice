class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        listchar = list(s)

        for i in range(0, len(listchar), 2*k):
            listchar[i:i+k] = reversed(listchar[i:i+k])
        
        return "".join(listchar)
        
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countWhite = 0 
        result = sys.maxsize
        fast = 0
        slow = 0
        n = len(blocks)

        for fast in range(n):
            if blocks[fast] == 'W':
                countWhite += 1
            
            if fast - slow + 1 == k:
                result = min(result, countWhite)
                if blocks[slow] == 'W':
                    countWhite -= 1
            
                slow += 1
            
        return result
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        T = 2 * n - 2
        N = time % T


        if N < n:
            return N + 1
        else:
            return T + 1 - N
        

        
        

        
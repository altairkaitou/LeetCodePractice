class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum, bobSum = 0, 0

        for i in range(len(aliceSizes)):
            aliceSum += aliceSizes[i]
        

        for j in range(len(bobSizes)):
            bobSum += bobSizes[j]
        
        diff_sum = (aliceSum - bobSum) // 2

        for candy2 in bobSizes:
            candy1 = diff_sum + candy2
            if candy1 in aliceSizes:
                return [candy1, candy2]
            




        
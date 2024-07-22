class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        totalSum = 0
        for num in nums:
            totalSum += num
        
        Subsequence = []
        SubSum = 0

        for num in nums:
            SubSum += num
            Subsequence.append(num)
            if SubSum > totalSum - SubSum:
                break

        return Subsequence
        
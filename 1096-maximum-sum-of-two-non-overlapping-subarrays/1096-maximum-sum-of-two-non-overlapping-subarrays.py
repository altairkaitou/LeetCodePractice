class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        count = 0

        prefix_sum = [0] * (len(nums))
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            prefix_sum[i] = curr_sum

        count_sub = 2
        max_sum = 0

        while count_sub > 0:
            count_sub -= 1

            for i in range(len(nums) - firstLen + 1):
                sum1 = prefix_sum[i + firstLen - 1]
                if i > 0:
                    sum1 -= prefix_sum[i - 1] 
                
                for j in range(i + firstLen, len(nums) - secondLen + 1):
                    sum2 = prefix_sum[j + secondLen - 1]
                    if j > 0:
                        sum2 -= prefix_sum[j - 1]
                    max_sum = max(max_sum, sum1 + sum2) 

            firstLen, secondLen = secondLen, firstLen
        return max_sum

        
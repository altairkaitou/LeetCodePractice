class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        if len(nums) <= 1 or k == 1:
            return 0

        nums.sort()
        res = float('inf')
        k -= 1

        for i in range(len(nums) - k):
            res = min(res, nums[i + k] - nums[i] )

        return res


        

            

        
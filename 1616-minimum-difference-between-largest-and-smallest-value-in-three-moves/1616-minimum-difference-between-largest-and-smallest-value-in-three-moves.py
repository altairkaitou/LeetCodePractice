class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) <= 4:
            return 0 

        diff1 = nums[-4] - nums[0]
        diff2 = nums[-3] - nums[1]
        diff3 = nums[-2] - nums[2]
        diff4 = nums[-1] - nums[3]

        return min(diff1,diff2,diff3,diff4)

        
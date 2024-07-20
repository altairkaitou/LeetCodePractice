class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        num_max1 = nums[-1]
        num_max2 = nums[-2]

        num_min1 = nums[0]
        num_min2 = nums[1]

        return (num_max1 * num_max2) - (num_min1 * num_min2)

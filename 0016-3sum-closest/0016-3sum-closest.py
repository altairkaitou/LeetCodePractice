class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        minDiff = float('inf')
        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                elif sum < target:
                    j += 1
                else:
                    k -= 1
                diff = abs(sum - target)
                while (diff < minDiff):
                    result = sum 
                    minDiff = diff
        return result
                

                

        
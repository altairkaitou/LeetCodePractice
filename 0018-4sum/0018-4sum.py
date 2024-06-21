class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        quad = []
        if len(nums) < 4:
            return quad 
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum == target:
                        quad.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
        return quad 
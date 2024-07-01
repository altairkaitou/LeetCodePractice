class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        min_length = len(set(nums))

        result = 0

        for i in range(len(nums)):
            sub_set = set()
            for j in range(i, len(nums)):
                sub_set.add(nums[j])
                if len(sub_set) == min_length:
                    result += 1
        return result

        
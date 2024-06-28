class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        index_count = {}

        for i in range(len(nums)):
            if nums[i] in index_count:
                if abs(i - index_count[nums[i]]) <= k:
                    return True
                
            index_count[nums[i]] = i
        return False
        
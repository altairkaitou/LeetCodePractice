class Solution:
    def findLHS(self, nums: List[int]) -> int:
        number_map = {}
        max_length = 0

        for num in nums:
            number_map[num] = number_map.get(num, 0) + 1
        
        for num in nums:
            if num + 1 in number_map:
                max_length = max(max_length, number_map[num] + number_map[num + 1])
        
        return max_length


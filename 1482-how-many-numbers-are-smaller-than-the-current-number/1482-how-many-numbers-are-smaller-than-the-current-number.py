class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)

        hash_tab = {}
        result = []

        for i, num in enumerate(sorted_num):
            if num not in hash_tab:
                hash_tab[num] = i

        for num in nums:
            result.append(hash_tab[num])
        
        return result




        
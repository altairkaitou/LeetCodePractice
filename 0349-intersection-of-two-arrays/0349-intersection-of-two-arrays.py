class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        result = []

        for i,n in enumerate(nums1):
            hashMap[n] = i
        
        for i in nums2:
            if i in hashMap and i not in result:
                result.append(i)
        
        return result
        
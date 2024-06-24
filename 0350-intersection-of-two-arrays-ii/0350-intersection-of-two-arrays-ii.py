class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorteds1 = nums1.sort()
        sorteds2 = nums2.sort()

        result = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i+= 1
            elif nums1[i] > nums2[j]:
                j += 1
            
            else:
                result.append(nums1[i])
                i+=1
                j +=1
        
        return result 
        
        
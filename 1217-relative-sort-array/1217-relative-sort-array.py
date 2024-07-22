class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []

        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    result.append(arr1[j])
                    arr1[j] = -1
        
        remain = [x for x in arr1 if x != -1]
        
        remain.sort()
        
        result.extend(remain)
        
        return result
        
        
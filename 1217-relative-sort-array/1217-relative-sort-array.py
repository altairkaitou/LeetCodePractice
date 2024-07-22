class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []

        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    result.append(arr1[j])
                    arr1[j] = -1
        
        remain = []

        for i in range(len(arr1)):
            if arr1[i] > -1:
                remain.append(arr1[i])
        
        remain.sort()
        
        for value in remain:
            result.append(value)
        
        return result
        
        
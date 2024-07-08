class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numbers = set()

        for num in arr:
            if (2 * num in numbers) or (num // 2 in numbers and num % 2 == 0):
                return True
            else:
                numbers.add(num)
        
        return False
        
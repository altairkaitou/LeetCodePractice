class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def sorted_key(array_x):
            return (bin(array_x).count('1'), array_x)
        

        arr.sort(key=sorted_key)

        return arr

        
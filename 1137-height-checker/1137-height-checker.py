class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                count += 1
        

        return count


        
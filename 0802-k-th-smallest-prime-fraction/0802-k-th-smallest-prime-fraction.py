class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []

        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                heappush(minHeap, (arr[i] / arr[j], (arr[i], arr[j])))
        
        for _ in range(k):
            a, b = heappop(minHeap)[1]
        
        return [a,b]
        
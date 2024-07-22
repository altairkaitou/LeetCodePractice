class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hash_map = defaultdict(int)

        for value, weight in items1:
            hash_map[value] += weight
        
        for value, weight in items2:
            hash_map[value] += weight
        

        result = [[value, weight] for value, weight in hash_map.items()]

        result.sort(key=lambda x: x[0])

        return result   

        
        
        
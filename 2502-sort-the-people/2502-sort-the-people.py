class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []

        for i in range(len(names)):
            res.append([names[i], heights[i]])
        
        res = sorted(res, key = lambda x: -x[1])

        sorted_name = [x[0] for x in res]
        return sorted_name


        
        
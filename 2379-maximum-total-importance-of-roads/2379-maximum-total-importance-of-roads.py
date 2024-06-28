class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        connections = [0] * n
        for road in roads:
            connections[road[0]] += 1
            connections[road[1]] += 1

        cities = list(range(n))

        def sortcity(city):
            return -connections[city]
        
        cities.sort(key = sortcity)
        value_cities = [0] * n
        current_value = n
        for city in cities:
            value_cities[city] = current_value
            current_value -= 1
        
        sum_result = 0
        for road in roads:
            sum_result += value_cities[road[0]] + value_cities[road[1]]
        
        return sum_result



        
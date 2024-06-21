class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        defaults = 0
        Extra = 0
        temp = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                defaults += customers[i]
            elif grumpy[i] == 1 and i < minutes:
                temp += customers[i]

        Extra = temp
        
        for j in range(minutes, len(customers)):
            temp += customers[j] * grumpy[j]
            temp -= customers[j - minutes] * grumpy[j - minutes]

            Extra = max(Extra, temp)
        
        return defaults + Extra 
            

        
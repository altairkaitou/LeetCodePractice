class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        numbers = {}
        current_number = n

        while True:
            for i in str(current_number):
                sum += int(i) ** 2
            
            if sum == 1:
                return True
            if sum in numbers:
                return False
            
            numbers[sum] = 0
            current_number = sum 
            sum = 0
        

        
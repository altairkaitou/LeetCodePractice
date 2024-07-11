class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        result = 0

        for i in range(len(students)):
            result += abs(students[i] - seats[i])
        
        return result

        
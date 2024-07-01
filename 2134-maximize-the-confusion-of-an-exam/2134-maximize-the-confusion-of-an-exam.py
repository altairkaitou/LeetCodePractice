class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_freq = 0
        result = 0

        count = Counter()

        for i in range(len(answerKey)):
            count[answerKey[i]] += 1
            max_freq = max(max_freq, count[answerKey[i]])

            if result - max_freq < k:
                result += 1
            
            else:
                count[answerKey[i - result]] -= 1

        return result

        
        
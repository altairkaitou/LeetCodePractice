class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result = 0
        idx = 0

        freq = Counter()

        for i, ch in enumerate(s):
            freq[ch] += 1

            while freq[ch] == 3:
                freq[s[idx]] -= 1
                idx += 1
            
            result = max(result, i - idx + 1)
        
        return result


        
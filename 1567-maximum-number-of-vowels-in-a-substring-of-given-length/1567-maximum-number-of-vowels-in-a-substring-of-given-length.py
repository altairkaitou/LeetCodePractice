class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = ['a','e','i','o','u']
        m_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
                m_vowels = max(m_vowels,count)
        
        left = 0
        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1
            if s[left] in vowels and k > 1:
                count -= 1
            left += 1
            m_vowels = max(m_vowels, count)
        
        return min(m_vowels, k)
        
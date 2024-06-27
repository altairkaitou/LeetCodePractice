class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest_nice = ""
        start = 0

        def isNice(char_map):
            isUpper = set(c for c in char_map if c.isupper())
            isLower = set(c for c in char_map if c.islower())
            return all(c.lower() in isLower for c in isUpper) and all(c.upper() in isUpper for c in isLower)

        for start in range(len(s)):
            char_map = {}

            for end in range(start, len(s)):
                char_map[s[end]] = char_map.get(s[end], 0) + 1

                if isNice(char_map):
                    if end - start + 1 > len(longest_nice):
                        longest_nice = s[start:end + 1]
                
        return longest_nice





        
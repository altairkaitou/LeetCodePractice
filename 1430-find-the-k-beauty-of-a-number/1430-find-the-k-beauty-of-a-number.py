class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)

        count = 0
        if len(s) == 1:
            return 1
        for i in range(len(s) - k + 1):
            x = int(s[i: i + k])

            if (x != 0 and num % x == 0):
                count += 1

        return count









        
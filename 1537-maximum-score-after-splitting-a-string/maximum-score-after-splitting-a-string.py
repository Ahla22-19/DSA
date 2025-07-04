class Solution:
    def maxScore(self, s: str) -> int:

        ans = 0
        ones = s.count("1")
        zeroes = 0

        for i in range(len(s) - 1):

            if s[i] == "0":
                zeroes += 1
            else:
                ones -= 1

            ans = max(ans, zeroes + ones)

        return ans

        
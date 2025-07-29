class Solution:
#     O(n) || O(1)
# Runtime: 30ms 90.00% || Memory: 13.9mb 10.00%
    def solution_1624_2(self, string: str) -> str:
        strAlphaFreq = [0] * 26

        for char in string:
            index = ord(char) - ord('a')

            strAlphaFreq[index] += 1

            if strAlphaFreq[index] > 1:
                return char
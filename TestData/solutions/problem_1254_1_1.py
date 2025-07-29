class Solution:
    def solution_1254_1_1(self, s: str) -> str:

        ans = ""

        def solution_1254_1_2(char, num):
            return chr(ord(char) + int(num))

        for index in range(len(s)):
            ans += solution_1254_1_2(s[index-1], s[index]) if index % 2 else s[index]

        return ans
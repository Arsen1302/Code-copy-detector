class Solution:
    def solution_200_4(self, s: str, t: str) -> str:
        ans = 0
        for i in range(len(s)):
            ans = ans ^ ord(s[i]) ^ ord(t[i])
        ans ^= ord(t[-1])
        return chr(ans)
class Solution:
    def solution_1123_3(self, n: int, k: int) -> str:
        ans = ''
        while (n - 1) * 26 >= k:
            ans += 'a'
            n -= 1; k -= 1
        ans += chr(ord('a') + (k % 26 or 26) - 1)
        ans += 'z' * (n - 1)
        return ans
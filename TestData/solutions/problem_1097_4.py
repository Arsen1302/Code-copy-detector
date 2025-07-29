class Solution:
    def solution_1097_4(self, s: str) -> int:
        ans = -1
        hashmap = {}
        for i, ch in enumerate(s):
            if ch not in hashmap:
                hashmap[ch] = i
            else:
                ans = max(ans, i - hashmap[ch] - 1)
        return ans
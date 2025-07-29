class Solution:
    def solution_77_2(self, columnTitle: str) -> int:
        ans = 0
        for i in columnTitle:
            ans = ans * 26 + ord(i) - ord('A') + 1
        return ans
class Solution:
    def solution_1502_2(self, words: List[str], pref: str) -> int:
        ans = 0
        for i in words:
            if i[:len(pref)] == pref:
                ans += 1
        return ans
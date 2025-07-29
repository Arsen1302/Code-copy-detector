class Solution:
    def solution_1339_4(self, s: str, words: List[str]) -> bool:
        ans = ''
        for i in words:
            ans += i
            if ans == s :
                return True
        return False